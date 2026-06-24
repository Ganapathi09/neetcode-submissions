class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
         # check if grouping is possible
        if len(hand) % groupSize != 0:
            return False

        # count all cards and insert it 
        count = Counter(hand)

        # try to form groups from smallest card
        for card in sorted(hand):

            if count[card] == 0:
                continue # to avboid resuse

            # build a consecutive group
            for i in range(groupSize):

                if count[card + i] == 0:
                    return False #if next card is 0 then we canot build 

                count[card + i] -= 1

        return True              
        