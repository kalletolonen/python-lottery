from drawNumbers import numbers_for_today;
import numpy as np;

# Randomize rows of Lotto numbers
def simulate_tickets(tickets):

	lotto_rows = np.random.randint(1,41,(tickets, 7))
	return lotto_rows;
