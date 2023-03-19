# python3
def min_heap(i, swaps, data, n):
    a=i
    if (2*i+1<n) and (data[2*i+1]<data[a]):
        a=2*i+1
    if (2*i+2<n) and (data[2*i]<data[a]):
        a=2*i+2
    if i != a:
        swaps.append((i, a))
        b = data[a]
        data[a] = data[i]
        data[i]=b
        return a
    else:
        return i



def build_heap(data):
    swaps = []

    n = len(data)

    for i in range(n//2, -1, -1):
      
      while True:
        c = min_heap(i, swaps,data,n)
        if c!=i:
            i=c;
        else:
            i=c
            break;
        


    
    return swaps


def main():
     # TODO : add input and corresponding checks
      # add another input for I or F 
      # first two tests are from keyboard, third test is from a file
      wait = input()
      littleshit = False
      if("I" in wait) :
          # input from keyboard
          n = int(input())
          data = list(map(int, input().split()))
          littleshit = True
  
      if("F" in wait):
          name = "tests/" + input()
          if not("a" in name):
              littleshit = True
              with open(name) as file:
                  # input from keyboard
                  n = int(next(file))
                  for line in file:
                      data= list([int(i) for i in line.split()])
                      
      if littleshit:
          # checks if lenght of data is the same as the said lenght
          assert len(data) == n
          # calls function to assess the data 
          # and give back all swaps
          swaps = build_heap(data)
           # output all swaps
          print(len(swaps))
          for i, j in swaps:
              print(i, j)
  
          
  
      
  
  
      # TODO: output how many swaps were made, 
      # this number should be less than 4n (less than 4*len(data))


   

if __name__ == "__main__":
    main()