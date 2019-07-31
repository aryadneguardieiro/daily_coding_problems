def string_to_list(s):
  try:
    if s == "[]":
      return []
    else:
      return list(map(float, s.strip('[]').split(',')))
  except:
    print("Can not convert {} to float list".format(s))
  return None