# Merge CSDH data

from pathlib import Path

import pandas as pd

this_dir = Path(__file__).parent

dfs = []
res = sorted(this_dir.glob('Learning Model Data*/*.csv'))
for state_csv in sorted(this_dir.glob('Learning Model Data*/*.csv')):
    dfs.append(pd.read_csv(state_csv))

all_df = pd.concat(dfs)
all_df.to_csv(this_dir / 'learning_models.csv', index=None)
