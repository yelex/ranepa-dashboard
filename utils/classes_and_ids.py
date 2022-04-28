import pandas as pd

PATH = '../files/classes and ids.xlsx'

def get_classes_and_ids(path = PATH) -> pd.DataFrame:
  return pd.read_excel(io = path)

def get_ids_vs_codes() -> pd.DataFrame:
  df = get_classes_and_ids()
  codes_ids = df.loc[df.RosstatId.notna(), ['ClassCode','RosstatId']]
  codes_ids.loc[:, 'RosstatId'] = codes_ids['RosstatId'].astype(int)
  codes_ids = codes_ids.set_index('RosstatId')
  return codes_ids

def get_codes_description(num_levels = 3) -> pd.DataFrame:
  df = get_classes_and_ids()
  regex_pattern = '^(\d+\.){' + str(num_levels-1) + '}\d+$'
  return df[df.ClassCode.str.match(regex_pattern)].set_index('ClassCode').loc[:, ['Description']]