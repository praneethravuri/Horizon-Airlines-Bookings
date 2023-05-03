from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint
from pymongo import MongoClient
import matplotlib.pyplot as plt
import os
import networkx as nx

client = MongoClient('mongodb://localhost:27017/')
db = client['airportDB']
users = db['users']
flights = db["flights"]
bookings = db["bookings"]
discount = db["discount"]

visualization_bp = Blueprint('visualization', __name__)


@visualization_bp.route("/visualization")
def visualization():

    query = flights.aggregate([{'$project':
                                {'_id': 0,
                                 'fromLocation': '$flight_details.fromLocation',
                                 'toLocation': '$flight_details.toLocation'
                                 }}])

    from_locations_dict = {}
    for res in query:
        key = (res['fromLocation'])
        from_locations_dict[key] = from_locations_dict.get(key, 0) + 1
    from_locations_dict = dict(
        sorted(from_locations_dict.items(), key=lambda item: item[1], reverse=True))
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(list(from_locations_dict.keys()),
            list(from_locations_dict.values()))
    ax.set_title('Number of Flights from Different Locations')
    ax.set_xlabel('Number of Flights')
    ax.set_ylabel('Location')
    save_location = os.path.join(
        os.getcwd(), 'static', 'images', 'fromLocation.png')
    directory = os.path.dirname(save_location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(save_location)


    query = flights.aggregate([{'$project': 
                            {'_id': 0,
                             'fromLocation': '$flight_details.fromLocation',
                             'toLocation': '$flight_details.toLocation'
                            }}])

    to_locations_dict = {}

    for res in query:
        key = (res['toLocation'])
        to_locations_dict[key] = to_locations_dict.get(key, 0) + 1
        
    to_locations_dict = dict(sorted(to_locations_dict.items(), key=lambda item: item[1], reverse=True))
    fig, ax = plt.subplots(figsize=(12, 6))

    # Create a horizontal bar chart
    ax.barh(list(to_locations_dict.keys()), list(to_locations_dict.values()))

    # Add title and labels
    ax.set_title('Number of Flights to Different Locations')
    ax.set_xlabel('Number of Flights')
    ax.set_ylabel('Location')
    save_location = os.path.join(
    os.getcwd(), 'static', 'images', 'toLocation.png')
    directory = os.path.dirname(save_location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(save_location)

    query = flights.aggregate([{'$project': 
                            {'_id': 0,
                             'fromLocation': '$flight_details.fromLocation',
                             'toLocation': '$flight_details.toLocation'
                            }}])

    source_destination = []

    for res in query:
        source_destination.append((res['fromLocation'],res['toLocation']))

    G = nx.DiGraph()

    # Define the edges
    edges = source_destination

    # Add the edges to the graph
    G.add_edges_from(edges)

    # Define the position of each node using a layout algorithm
    pos = nx.spring_layout(G)

    # Draw the nodes and edges
    fig, ax = plt.subplots(figsize=(20, 10))
    nx.draw_networkx_nodes(G, pos, node_size=2000)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")
    plt.axis("off")
    save_location = os.path.join(
    os.getcwd(), 'static', 'images', 'connected_flights.png')
    directory = os.path.dirname(save_location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(save_location)


    return render_template("visualization.html")
