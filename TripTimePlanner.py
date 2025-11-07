#!/usr/bin/env python3

# Thanksgiving Shopping Trip Optimizer

def optimize_trip(items, available_time):
    """
    Optimizes shopping trip by grouping items by store and calculating total time.
    
    Args:
        items: List of dicts with keys: name, store, store_time, drive_time
        available_time: Total minutes available for shopping
    
    Returns:
        Optimized route with time breakdown
    """
    
    # Group items by store
    stores = {}
    for item in items:
        store_name = item['store']
        if store_name not in stores:
            stores[store_name] = {
                'store': store_name,
                'items': [],
                'total_store_time': 0,
                'drive_time': item['drive_time']
            }
        stores[store_name]['items'].append(item['name'])
        stores[store_name]['total_store_time'] += item['store_time']
    
    # Sort by drive time (visit closest first)
    route = sorted(stores.values(), key=lambda x: x['drive_time'])
    
    # Calculate total time
    total_time = sum(stop['drive_time'] + stop['total_store_time'] for stop in route)
    
    # Print route
    print("\n" + "="*60)
    print("OPTIMIZED THANKSGIVING SHOPPING ROUTE")
    print("="*60)
    
    for i, stop in enumerate(route, 1):
        print(f"\nStop {i}: {stop['store']}")
        print(f"  Items: {', '.join(stop['items'])}")
        print(f"  Drive time: {stop['drive_time']} min")
        print(f"  Shopping time: {stop['total_store_time']} min")
        print(f"  Stop total: {stop['drive_time'] + stop['total_store_time']} min")
    
    print("\n" + "="*60)
    print(f"TOTAL TRIP TIME: {total_time} minutes")
    print(f"AVAILABLE TIME: {available_time} minutes")
    
    if total_time <= available_time:
        print(f"✓ SUCCESS! You have {available_time - total_time} minutes to spare")
    else:
        print(f"✗ WARNING! You need {total_time - available_time} more minutes")
    print("="*60 + "\n")
    
    return route, total_time


# Example shopping list
shopping_items = [
    {'name': 'Turkey', 'store': 'Grocery Store', 'store_time': 30, 'drive_time': 15},
    {'name': 'Pumpkin Pie', 'store': 'Bakery', 'store_time': 10, 'drive_time': 20},
    {'name': 'Cranberry Sauce', 'store': 'Grocery Store', 'store_time': 5, 'drive_time': 15},
    {'name': 'Fresh Rolls', 'store': 'Bakery', 'store_time': 5, 'drive_time': 20},
    {'name': 'Green Beans', 'store': 'Grocery Store', 'store_time': 10, 'drive_time': 15},
    {'name': 'Wine', 'store': 'Liquor Store', 'store_time': 15, 'drive_time': 10}
]

# Available time in minutes
available_minutes = 120

# Run optimizer
route, total = optimize_trip(shopping_items, available_minutes)

# To add your own items, modify the shopping_items list above:
# {'name': 'Item Name', 'store': 'Store Name', 'store_time': minutes, 'drive_time': minutes}

