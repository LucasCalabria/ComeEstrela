# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    size(640, 360)
    velocity_vehicle = PVector(0, 0)
    velocity_food = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity_vehicle)
    food = Food(width / 5, height / 5, velocity_food)
    

def draw():
    background(137, 23, 188, 0.82)
    position = food.getPosition()
    food.update()
    food.display()
    vehicle.update()
    vehicle.display()
    vehicle.arrive(position)
    if (food.getPosition().dist(vehicle.getPosition()) <= 7):
        food.collision()
    
