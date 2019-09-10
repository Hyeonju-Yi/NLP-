class TourInfo:
    title = None;  price = None;  comment = None
    review_score = None;  travel_period = None;  departure_period = None
    
    def __init__(self, title, price, comment, 
                 review_score, travel_period, departure_period):
        self.title = title;  self.price = price;  self.comment = comment
        self.review_score = review_score;  self.travel_period = travel_period
        self.departure_period = departure_period
        
    def __str__(self):
        return '%s, %d, %s, %f, %s, %s' \
            % (self.title, self.price, self.comment, self.review_score, self.travel_period, self.departure_period)