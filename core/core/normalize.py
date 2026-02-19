def norm_reid(x): return min(x / 100.0, 1.0)
def norm_value(v): return {"low":0.3,"medium":0.6,"high":0.9}[v]
def norm_sensitivity(s): return {"low":0.2,"moderate":0.5,"high":0.8}[s]
