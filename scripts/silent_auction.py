

class SilentAuction:
    def __init__(self):
        self.is_any_bidder = True
        self.bid_entries = dict()

    def get_user_entries(self):
        user_name = input('What is you name?:\n')
        user_bid = input('Please enter your bid...\n')
        self.bid_entries[user_name] = user_bid
    
    def check_remaining_bidder(self):
        bidder_queue = input('Is there anymore bidder? Please provide your answer as "yes" or "no".\n')
        if bidder_queue == "no":
            self.is_any_bidder = False

    def get_highest_bidder(self):
        return max(self.bid_entries, key = self.bid_entries.get)

    def auction(self):
        while self.is_any_bidder:
            self.get_user_entries()
            self.check_remaining_bidder()
        
        higest_bidder = self.get_highest_bidder()
        print(f"Congratulation! {higest_bidder}. You have the highest bid of ${self.bid_entries[higest_bidder]}")

if __name__ == "__main__":
    silent_auction = SilentAuction()
    silent_auction.auction()
    

