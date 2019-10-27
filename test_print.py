from contextlib import redirect_stdout
import io

b = io.BytesIO()
with redirect_stdout(b):
    print("hello!", 'utf-8')  # output of STT engine here