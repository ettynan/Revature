'''Handles all dealership operations'''
import sys
from project0.users.model import User
from project0.vehicles.model import Vehicle
from project0.offers.model import Offer

from project0.data.logger import get_logger
import project0.data.mongo as db

_log = get_logger(__name__)

def create_new_user():
    '''Registers the user in the app - creates new instance of User'''
    new_user = {}
    new_user['username'] = input('Username: ')
    new_user['password'] = input('Password: ')
    new_user['firstname'] = input('First name: ')
    new_user['lastname'] = input('Last name: ')
    new_user['role'] = input('Role (employee or customer): ')
    return User.from_dict(new_user)

def create_new_vehicle(user):
    '''Prompts Employee to create new instance of vehicle class'''
    new_vehicle = {}
    new_vehicle['make'] = input('Make: ')
    new_vehicle['model'] = input('Model: ')
    new_vehicle['year'] = input('Year: ')
    new_vehicle['color'] = input('Color: ')
    new_vehicle['price'] = float(input('Price: '))
    return Vehicle.from_dict(new_vehicle)

def create_new_offer(user, vehicle):
    '''Prompts Employee to create new instance of offer class
        user and vehicle are tied to offer i.e. a user is making
        an offer on a specific vehicle'''
    new_offer = {}
    new_offer['offer_amount'] = input('Offer amount (q to quit): ')
    new_offer['customer_id'] = user.get_id()
    return Offer.from_dict(new_offer)

def list_items(lst):
    '''Function to print out a numbered list when given a list'''
    for i, item in enumerate(lst):
        print(i, item, sep=': ')

def get_all(item):
    '''Receives string identifying type and returns list of all that type'''
    if item == 'vehicle':
        return db.get_vehicles()
    else:
        print('Invalid Selection')
        return None

def add_item(item: str, user=None, vehicle=None):
    '''Receives vehicle and user obj and str arg
    prompts the user for the fields of the desired item'''
    if item == 'user':
        new_user = create_new_user()
        db.insert_item(new_user)
    elif item == 'vehicle':
        db.insert_item(create_new_vehicle(user))
    elif item == 'offer':
        offer = create_new_offer(user, vehicle)
        db.insert_item_offer(offer, vehicle)
    else:
        print('Invalid Selection')

def remove_item(item):
    '''Removes a item from the object'''
    if item == 'vehicle':
        available = db.get_available_vehicles()
        list_items(available)
        sel = input('\nWhat vehicle do you want to remove?: ')
        vehicle = available[int(sel)]
        item_type = type(vehicle).__name__
        db.delete_item(item_type, vehicle)
    else:
        print('Invalid Selection')

def get_owner_vehicles(person: User):
    '''Takes in a user, find their owned vehicles, returns them'''
    print('Vehicles owned:')
    vehicle_list = []
    for v_id in person.get_owned_vehicles():
        vehicle = db.get_vehicles_by_id(v_id)
        vehicle_list.append(vehicle)
    list_items(vehicle_list)
    return vehicle_list

def get_pending_offers(vehicle: Vehicle):
    '''Returns offers on a vehicle'''
    offers_for_vehicle = list(filter(lambda offer: offer.get_status()
                                     == 'pending', vehicle.get_offers()))
    return offers_for_vehicle

def enter_platform(person: User):
    '''Prompts user for selection, taking them to the respective platrform options'''
    if person:
        _log.info('Logging in as %s', person.username)
    while person:
        option = input('Make a selection: 1. Employee, 2. Customer,  3. Quit: ')
        if option == '3':
            break
        elif option == '1':
            if person.get_role() == 'employee':
                employee_ops(person)
            else:
                print('Not an employee')
        elif option == '2':
            if person.get_role():
                customer_ops(person, option)
        else:
            print('Not a valid option')

def customer_ops(person: User, vehicle: Vehicle):
    '''Prompts customer for imput of which system item they wish to do'''
    while True:
        print('\n1. View Vehicles', '2. Make Offer', '3. View Owned',
                '4. Remaining Payments', '5. Quit', sep='\n')
        option = (input('\nChoose an option: '))
        try:
            option = int(option)
        except ValueError:
            _log.info('Invalid digit')
            print('Need to enter a number')
        if option == 1:
            print('\nVehicles on lot: ')
            list_items(db.get_vehicles())
            print("\nAnd below are the vehicles still available")
            list_items(db.get_available_vehicles())
        elif option == 2:
            item = 'offer'
            print('Available vehicles to purchase: ')
            list_items(db.get_available_vehicles())
            available = db.get_available_vehicles()
            vehicle_choice = input("\nPick a vehicle q to quit: ")
            if vehicle_choice == 'q':
                break
            try:
                vehicle_choice = int(vehicle_choice)
            except ValueError:
                print('Must enter a number.')
                _log.info('No vehicle could be found')
                return None
            if vehicle_choice > len(available):
                print('Must enter number in range.')
                _log.info('No offer could be found')
                return None
            vehicle = available[vehicle_choice]
            add_item(item, person, vehicle)
        elif option == 3:
            get_owner_vehicles(person)
        elif option == 4:
            show_payments_remaining(person, vehicle)
        elif option == 5:
            break


def update_offer_status(offer, status):
    '''Sends the status to set_status'''
    offer.set_status(status)

def accept_helper(offers_list, offer_idx):
    '''Takes in an offer list and index and returns the offer after updating status'''
    offer_accept = offers_list[int(offer_idx)]
    for i, offer in enumerate(offers_list):
        if i is not offer_idx:
            offer.set_status('rejected')
    offer_accept.set_status('accepted')
    return offer_accept

def db_accept_helper(offer_accept, vehicle):
    '''Takes in an accepted offer and vehicle and updates the owned/owner in database'''
    buyer = db.get_user_by_id(offer_accept.get_customer_id())
    print('Car buyer: ')
    print(buyer)
    vehicle.set_owner(buyer.get_id())
    buyer.add_vehicle_owned(vehicle.get_id())
    db.update_user(buyer)
    db.update_offer(vehicle)

def accept_offer(vehicle: Vehicle):
    '''Changes the status of an offer to accept'''
    offers_list = get_pending_offers(vehicle)
    list_items(offers_list)
    offer_idx = input('Select offer to accept (q to quit): ')
    if offer_idx == 'q':
        return None
    try:
        offer_idx = int(offer_idx)
    except ValueError:
        _log.info('Not a valid selection')
        print('Invalid choice.')
        return None
    if offer_idx < len(offers_list):
        offer_accept = accept_helper(offers_list, offer_idx)
        db_accept_helper(offer_accept, vehicle)
    else:
        print('Invalid selection')


def monthly_payment_calc(new_price, term, vehicle):
    '''Takes in the offer amount as new_price, the term, and the vehicle and returns the monthly payment'''
    payment_total = 0
    splitted_str = vehicle.get_payments()
    if splitted_str == False:
        print('No payments made.')
    else:
        print('Payments made prior: ', splitted_str)
        splitted = []
        for value in vehicle.get_payments():
            splitted = value.split(',')
        for i in splitted:
            payment_total += float(i)
        print(payment_total)
        current_price = float(new_price) - float(payment_total)
        monthly_payment = float(current_price/term)
    return monthly_payment

def show_payments_remaining(user, vehicle):
    '''Takes in user and vehicle and shows payments they have.'''
    owned_vehicles = get_owner_vehicles(user)
    while True:
        vehicle_idx = input('Choose the car to see payments (q to quit): ')
        if vehicle_idx == 'q':
            break
        term = input('Term length q to quit: ')
        if term == 'q':
            break
        try:
            term = int(term)
        except ValueError:
            _log.info('Not a proper option.')
            print('Not an option')
            return None
        if int(vehicle_idx) < len(owned_vehicles):
            vehicle = owned_vehicles[int(vehicle_idx)]
            new_price = vehicle.get_accepted_offer_amount()
            print('new price: ', new_price)
            monthly_payment = monthly_payment_calc(new_price, term, vehicle)
            print('You have ' + str(term) + ' payments of $' + '{0:.2f}'.format(monthly_payment))
        else:
            print('No vehicles found')

def view_all_payments():
    '''View of all payments on all vehicles sold'''
    vehicle_lst = db.get_all_payments()
    for vehicle in vehicle_lst:
        print('Payments: ', vehicle.get_payments(), 'Sold vehicle id: ', vehicle.get_id())

def reject_offer(vehicle: Vehicle):
    '''Rejects an offer on a vehicle, updates the offer status'''
    offers = get_pending_offers(vehicle)
    _log.debug(type(offers))
    list_items(offers)
    option = input('Select offer to reject (q to quit): ')
    if option == 'q':
        return None
    elif int(option) < len(offers):
        offer_reject = offers[int(option)]
        offer_reject.set_status('rejected')
        db.update_offer(vehicle)
        return None
    else:
        print('Invalid option, try again')
        return None

def select_vehicle():
    '''Returns vehicle user selected from list'''
    list_items(db.get_available_vehicles())
    available = db.get_available_vehicles()
    vehicle_choice = input("\nPick a vehicle or q to quit: ")
    if vehicle_choice is 'q':
        sys.exit()
    try:
        vehicle_choice = int(vehicle_choice)
    except ValueError:
        print('Must enter a number.')
        _log.info('No offer could be found')
        return None
    if vehicle_choice > len(available):
        print('Must enter number in range.')
        _log.info('No offer could be found')
        return None
    vehicle = available[(vehicle_choice)]
    return vehicle

def employee_ops(person: User):
    '''Prompts employee for imput of which system item they which to do'''
    while True:
        print('\n1. Add Vehicle', '2. Show Vehicles', '3. Remove Vehicle', '4. Accept Offer',
              '5. Reject Offer', '6. View Payments', '7. Quit', sep='\n')
        option = (input('\nChoose an option: '))
        try:
            option = int(option)
        except ValueError:
            _log.info('Invalid digit')
            print('Need to enter a number in range')
        if option == 1:
            item = 'vehicle'
            add_item(item)
        elif option == 2:
            item_list = db.get_vehicles()
            list_items(item_list)
        elif option == 3:
            item = 'vehicle'
            remove_item(item)
        elif option == 4:
            select = select_vehicle()
            if select is None:
                break
            accept_offer(select)
        elif option == 5:
            select = select_vehicle()
            if select is None:
                break
            reject_offer(select)
        elif option == 6:
            view_all_payments()
        elif option == 7:
            break
        else:
            print('Not a proper option.')
            _log.info('Not a valid option.')
