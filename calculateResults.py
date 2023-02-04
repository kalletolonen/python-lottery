from drawNumbers import numbers_for_today;
from simulateTickets import simulate_tickets;
import time;

my_ticket_amount = int(input("How many rows would you like? "))
correct_numbers = numbers_for_today();
start_time_for_ticket_generation = time.time();
ticket_array = simulate_tickets(my_ticket_amount);
ticket_array.tolist();

print("Time elapsed for row generation: ", time.time() - start_time_for_ticket_generation
, "seconds");


print("Correct Lotto numbers are: ");
print(correct_numbers);
start_time_for_win_iteration = time.time();

def correct_in_categories():
	four_correct = 0;
	five_correct = 0;
	six_correct = 0;
	seven_correct = 0;
	set1 = set(correct_numbers);
	
	for arr in ticket_array:
		set2 = set(arr)
		similar_items = set1.intersection(set2);
		count = len(similar_items)
		if count == 4:
			four_correct += 1
		elif count == 5:
		    five_correct += 1
		elif count == 6:
		    six_correct += 1
		elif count == 7:
		    seven_correct += 1
	return four_correct, five_correct, six_correct, seven_correct
	

wins = correct_in_categories();

print("4 correct results: ",wins[0]);
print("5 correct results: ",wins[1]);
print("6 correct results: ",wins[2]);
print("7 correct results: ",wins[3]);

print("Time elapsed for result check: ", time.time() - start_time_for_win_iteration, "seconds");
