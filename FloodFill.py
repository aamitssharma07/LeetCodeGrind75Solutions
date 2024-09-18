class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: 

        #Defining Function for flood filling
        def fill(curr_row,curr_col):



            if(curr_row >= 0 and curr_row < max_rows and curr_col >= 0 and curr_col < max_cols ):#Thius condition chexks that the index should be in range
                if(image[curr_row][curr_col]==color or image[curr_row][curr_col] != start_pixel):#This is the main and nchor condition
                    return image
                else:
                    image[curr_row][curr_col]=color
                    fill(curr_row,curr_col+1)  # Right element
                    fill(curr_row+1,curr_col)  # Buttom element
                    fill(curr_row,curr_col-1)  # Left element
                    fill(curr_row-1,curr_col)  #Top Element
            

        max_rows = len(image)
        max_cols =  len(image[0])
        start_pixel = image[sr][sc]
        fill(sr,sc)
        return image






           
         
        