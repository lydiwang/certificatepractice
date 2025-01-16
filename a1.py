# We have added import math
# It's only needed once
import math

# Problem 1
#input radius r, height h
#return volume
def c(r,h):
    volume = (1/3)*(math.pi)*(r**2)*h
    return round(volume, 2)
    

    
# Problem 2
#input t days
#output oxygen conten percent of it normal level
def f(t):
    oxygen_content_percent = 100*(((t**2)+(10*t)+100)/((t**2)+(20*t)+100))
    return round(oxygen_content_percent, 2)

# Problem 3
#input t hours
#return percent watching tv
def P(t):
   watching_tv_percent = (0.01354*(t**4))-(0.49375*(t**3))+(2.58333*(t**2))+(3.8*t)+31.60704
   return round(watching_tv_percent, 2)

# problem 4
#input x percent
#return millions of dollars
def cost(x):
    millions_of_dollars = (0.5*x)/(100-x)
    return round(millions_of_dollars, 2)

# Problem 5
#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    child_dosage_mg = ((t+1)/24)*a
    return round(child_dosage_mg, 2)

# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def I(S):
   infected_children = (192*(math.log((S/762), 2))-S+763)
   return math.ceil(infected_children)

# Problem 7
#input number of items 
#output total cost 
# q > 0
def C(q):
    total_cost = (0.01*(q**3))-(0.6*(q**2))+(13*q)+1000
    return round(total_cost, 2)

#input number of items
#output average cost
def A(q):
    average_cost = (C(q)/q)
    return round(average_cost, 2)

# Problem 8
#input months t=0,...,11
#output items sold x 1000
def hh(t):
   sales_model = 532/ (1+869*math.exp(-1.33*t))
   return math.floor(sales_model)

# Problem 9
#input time seconds
#output feet
def height(t):
    h = -16*t**2 + 64*t + 80
    return round(h, 2)

# Problem 10
#input t hours
#output percent treatment
def B(t):
    treatment_benefit = (0.44*(t**4) + 700)/(0.1*(t**4) + 7)
    return round(treatment_benefit, 2)


# Problem 11
#input coefficients for quadratic and value
#output True if value is root, False otherwise
def quad(a,b,c,x):
    y = a*x**2 + b*x + c 
    if y==0:
        return True
    else:
        return False
    


# Problem 12 
#input P principle, n times per year, t years, r rate
#output dollars
def R(P,r,n,t):
    sinking_fund = P*(((1+(r/n))**(n*t)-1)/(r/n))
    return round(sinking_fund, 2)

#Problem 13
#input dimensions w,l,h for width, length, height of a 
# rectangular solid
#output total surface area
def S(w,l,h):
    surface_area = 2*(l*w + l*h + w*h)
    return surface_area

#Problem 14
#input side s of a square
#output diagonal length 
def square_diagonal(s):
   diagonal_length = math.sqrt(2*(s**2))
   return diagonal_length

#input diagonal of a square
#output area of largest circle inscribed in square
def circle_area(d):
   r = (1/2)*d
   area = math.pi * ((r**2)/2)
   return round(area, 2)

#Problem 15
#input earned runs e, innings pitched i, total innings t
#output earned runs average
def ERA(e,i,t):
    earned_run_average = (e/i)*t
    return round(earned_run_average, 2)

#problem 16
#input temperature (F), wind speed (mph)
#output wind chill
def T_wc(temp,wind_speed):
    wind_chill_index = 35.74 + 0.6215*temp - 35.75*((wind_speed)**0.16) + 0.4275*temp*(wind_speed**0.16)
    return math.floor(wind_chill_index)

#problem 17
#input n
#output approximate to n!
def fact_est(n):
    nf = math.sqrt(2*math.pi*n)*((n/math.e)**n)
    return int(nf)


#problem 18
#input sphere volune
#output radius of the sphere
def volume_to_radius(v):   
    r = (((3*v)/(4*math.pi))**(1/3))
    return round(r, 2)

 
def side_max_square(v):
   side = math.sqrt((volume_to_radius(v)**2)/3)
   return round(side, 2)

#problem 19
#input list of market prices per share
#output a tuple containing average price and the last price
def app(market):
    market_price = sum(market)/len(market)
    y = market[-1]
    x = round(market_price, 2)
    return (x, y)


# problem 20
#input n
#ouptut return the value that would be returned from employee's model
def model1(n):
    model1 = 10*(n**3) - 35*(n**2) + 50*n -24
    return model1

# input n
#ouptut implement the more intutitve model yourself that can represent the values shown in equation 43 in the PDF
def model2(n):
    better_function = n*n*n*n
    return better_function

#input a tuple containing values
#output: tuple of tuples comparing the outputs from both models, as shown in sample output in the PDF.
# Example: ((x0, model1(x0), model2(x0)), (x1,model1(x1), model2(x1)), (x2,model1(x2), model2(x2)), (x3,model1(x3), model2(x3)), ((x4, model1(x4), model2(x4))
def compare_models(inputs):
    tuple = ()
    for i in inputs:
        tuple += (i, model1(i), model2(i)),
    return tuple
    




if __name__ == "__main__":
    """
    The following tests are given by us. For example, after completing problem 1, 
    you can uncomment the tests for problem 1 and run the a1.py file to see the output.
    Similarly, you can uncomment the tests for other problems as you complete them.
    
    If you want to do some of your own testing, you can also add them, for example if you want to
    test problem 1 then you can add another print statement and call c() function with your own
    input value to see the output of c() on that value -- print(c(5, 7)) or print(c(4, 47)) etc.
    
    Please remember to comment the test cases before submitting to the Autograder. You can use them 
    as long as you want while testing on your system, but please comment the below test cases before
    submitting to the Autograder.
    """

    #problem 1
    #volume of cone
    print(c(2,5)) 
    print(c(3,7))

    #problem 2
    #oxygen content
    print(f(0))
    print(f(10))

    #problem 3
    #tv watching
    print(P(0))
    print(P(3))
    print(P(8))

    #problem 4
    #toxic waste
    print(cost(50))
    print(cost(70))
    print(cost(90))

    #problem 5
    # cowling's rule
    print(D(4,500))
    
    #problem 6
    #flu outbreak
    S_6 = 100
    print(I(S_6))
    S_6 = 300
    print(I(S_6)) 

    #problem 7
    #average cost
    print(C(1))
    print(A(1))
    
    #problem 8
    print(hh(0))
    print(hh(5))
    print(hh(10))

    #problem 9
    print(height(5))
   
    #problem 10        
    #make your own inputs/outputs
    print(B(1))

    #problem 11
    #quadratic roots
    print(quad(2,5,-12,-4))
    print(quad(2,5,-12,3/2))
    print(quad(2,5,-12,1))

    # problem 12
    # Sinking Fund
    P = 22000
    n = 1
    t = 7
    r = 6/100
    print(R(P,r,n,t))
    P = 500
    n = 12
    t = 20
    r = 4/100
    print(R(P,r,n,t))
    P = 1200
    n = 4
    t = 10
    r = 8/100
    print(R(P,r,n,t))

    #problem 13
    #make your own inputs/outputs
    print(S(2,3,4))

    #problem 14
    s_13 = 10
    a_13  = circle_area(square_diagonal(s_13))
    print(a_13)

    #problem 15
    e_14,i_14,t_14 = 4,6,9
    print(ERA(e_14,i_14,t_14))

    
    #problem 16
    temp_15, wind_speed_15 = 2,5
    print(T_wc(temp_15,wind_speed_15))

    #problem 17
    n0_16 = 10
    print(math.factorial(n0_16),fact_est(n0_16))
    n0_16 = n0_16 * 10
    print(math.factorial(n0_16),fact_est(n0_16))
    
    #problem 18
    v = 268.08
    print(volume_to_radius(v), side_max_square(v))
    
    #problem 19
    market = [40 ,35 ,34 ,38 ,50]
    print(app(market))
    
    #problem 20
    inputs = (1,2,3,4,5)
    print(compare_models(inputs))
    
    