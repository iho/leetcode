class TrafficLight:
    def __init__(self):
        
        self.is_green_on_main_road = True

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        # // 1,2
        # // 3,4 
        print(carId, roadId, direction)
            
        if roadId==1:
            if self.is_green_on_main_road:
                crossCar()
            else:
                turnGreen()
                self.is_green_on_main_road = True
                crossCar()
        elif roadId==2:
            if self.is_green_on_main_road:
                turnGreen()
                self.is_green_on_main_road = False
                crossCar()
            else:
                crossCar()
            
            