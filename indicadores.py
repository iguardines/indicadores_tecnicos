def devolver_con_percentil(df):
  data = df . copy()
  data["variacion"]  = data["Close"].pct_change() * 100 
  data.dropna(inplace=True)
  data["rank_variacion"] = data["variacion"].rank()
  data["rank_variacion_pct"] = data["variacion"].rank(pct= True)
  return data

def devolver_top_n_variacion(df, n=10, es_de_baja=True):
  data = df . copy() 
  data["variacion"]  = data["Close"].pct_change() * 100 
  data.dropna(inplace=True)
  return data.sort_values("variacion", ascending = es_de_baja ).head(n)
