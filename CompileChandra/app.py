from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os
import uuid

app = Flask(__name__)
CORS(app)

LANG_COMMANDS = {
    'c': {
        'ext': '.c',
        'compile': lambda src, exe: ['gcc', src, '-o', exe],
        'run': lambda exe: [exe],
    },
    'cpp': {
        'ext': '.cpp',
        'compile': lambda src, exe: ['g++', src, '-o', exe],
        'run': lambda exe: [exe],
    },
    'python': {
        'ext': '.py',
        'run': lambda src: ['python3', src],
    },
    'javascript': {
        'ext': '.js',
        'run': lambda src: ['node', src],
    },
}

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code')
    lang = data.get('language')
    if not code or not lang or lang not in LANG_COMMANDS:
        return jsonify({'error': 'Invalid input'}), 400

    lang_info = LANG_COMMANDS[lang]
    ext = lang_info['ext']
    temp_dir = tempfile.mkdtemp()
    filename = f'Main{ext}'
    filepath = os.path.join(temp_dir, filename)
    with open(filepath, 'w') as f:
        f.write(code)

    output = ''
    error = ''
    try:
        if 'compile' in lang_info:
            exe_path = os.path.join(temp_dir, 'a.out') if lang != 'java' else filepath
            compile_cmd = lang_info['compile'](filepath, exe_path)
            compile_proc = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
            if compile_proc.returncode != 0:
                error = compile_proc.stderr
            else:
                run_cmd = lang_info['run'](exe_path)
                run_proc = subprocess.run(run_cmd, capture_output=True, text=True, timeout=10, cwd=temp_dir)
                output = run_proc.stdout
                error = run_proc.stderr
        else:
            run_cmd = lang_info['run'](filepath)
            run_proc = subprocess.run(run_cmd, capture_output=True, text=True, timeout=10, cwd=temp_dir)
            output = run_proc.stdout
            error = run_proc.stderr
    except Exception as e:
        error = str(e)
    finally:
        try:
            for f in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, f))
            os.rmdir(temp_dir)
        except Exception:
            pass
    return jsonify({'output': output, 'error': error})

if __name__ == '__main__':
    app.run(debug=True) 