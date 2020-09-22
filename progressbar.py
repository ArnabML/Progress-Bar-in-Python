from tqdm import tqdm , trange
import time

pbar = tqdm(total=100)
for i in range(10):
	time.sleep(0.3)
	pbar.update(10)
pbar.close()
