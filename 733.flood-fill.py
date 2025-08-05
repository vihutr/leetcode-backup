# @leet start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        matching_color = image[sr][sc]
        print(f'x, y: {len(image[0])}, {len(image)}')
        print(f'color: {color}, matching_color: {matching_color}')
        if matching_color != color and (0 <= sr < len(image[0])) and (0 <= sc < len(image)):
            self.fill(image, sr, sc, color, matching_color)
        return image
        
    def fill(self, image: List[List[int]], sr:int, sc:int, color:int, match:int):
        print(f'i: {sc}, j: {sr}')
        print(f'pixel current value: {image[sr][sc]}, matches?: {match}, change to: {color}')
        if image[sr][sc] == match:
            image[sr][sc] = color
            self.print2dList(image)
            if (sr + 1) < len(image):
                self.fill(image, sr + 1, sc, color, match)
            if (sr - 1) >= 0:
                self.fill(image, sr - 1, sc, color, match)
            if (sc + 1) < len(image[0]):
                self.fill(image, sr, sc + 1, color, match)
            if (sc - 1) >= 0:
                self.fill(image, sr, sc - 1, color, match)
        return
    
    def print2dList(self, l: List[List[int]]):
        for rows in l:
            print(rows)

# @leet end
