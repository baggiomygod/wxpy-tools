def log(func):
  def wrapper(*args, **kw):
    print('call %s():'%func.__name__)
    return func(*args, **kw)
  return wrapper


@log # 在输出签加上 call {__name__}:
def now():
  print('123')

now()

