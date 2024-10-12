import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("../workouts.csv")
query_engine = PandasQueryEngine(df=df, verbose=True)
response = query_engine.query(input("What exercises would you like to do? "))