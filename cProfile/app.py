import cProfile
import io
import pstats
from flask import Flask

app = Flask(__name__)

def cpu_intensive_function():
    # Simulate a CPU-intensive task
    result = 0
    for i in range(1000000):
        result += i * i
    return result

@app.route('/')
def index():
    pr = cProfile.Profile()
    pr.enable()
    result = cpu_intensive_function()
    pr.disable()

    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    return f"<pre>{s.getvalue()}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')