import sympy as sp #basically whenever we do sp.something itll be a function that sympy provides

class FunctionsManager: # basically creating a function with functions in it like i like to see it
    def __init__ (self): #as soon as class is "ran" this initialises and creates a list, self is needed for it to work (i still cant fully explain even after 30m of google) its smth to do with naming it and so it creates the list, no self means it stays in that "method" and doesnt get transfered as a variable or data to other functions in the call
        self.x = sp.symbols("x") #this line creates a symbolic variable called x not a python variable, something that math can be done with. 
        self.functions = [] #this is the list itself so when we do fm = functionmanager() and then add function it adds to here and it has its own vairable or smth so fm1 = functionmanager() is different

    def add_function(self, expression): #where it says self itll replace with that lists name so in this case fm and expression is the variable. so when we it runs self.functions.append its actually doign fm.functions.append and adding whatever we input to the end of the list "functions"
        expr = sp.sympify(expression)#this turns goofy ass x**2 into actual maths so x to the power of 2. symbolic expression not a string so we cana actually do maths with it :D
        self.functions.append(expr) #mentioned in the first line for this block append just chucks whatever variable we put inside add_function(^^^) to the end of the list simpyfied into a readable math shi
    
    def print_functions(self):#defining the function
        for func in self.functions:# for random "ass name" inside of the list self.functions() print one variable then go onto the next and print that
            print(func)
    
    def diff_functions (self):#defining the function to make it obvs what it does
        derivatives = [] #creating a list to store the derivatives after it calculates them
        for func in self.functions: # the self lets it refer to the previous list because its basically been stored (i think) then func is just a name we chose i think its smth like for every variable in this list but instead of every variable we call it func
            derivative = sp.diff(func, self.x)#couple things to digest derivative is the variable name its different to derivatives the list, sp.diff is the differentiste option in sympy which we imported as sp func is the same variable name so that it goes through every function in the function list and , self.x tells it to derive with respects to x
            derivatives.append(derivative) # lots of simmilar words but derivatives.append is just adding the derivative it calculated to the back of the list derivatives then it loops until no more functions left in the functions list
        return derivatives #returns the whole list of derivsatives and acts like a save button so it can be used for other things.
    def eval_functions(self,value): #defining the function to be used later to evaluate inputted functions to a value. basically working out y for a given x value
        results = [] #list to store the evaluated answer aka y values
        for func in self.functions: #refering to the list of functions and going through them all to evaluate and calc Y
            result = func.subs(self.x, value) #sympy function subs just substitutes the value we input for x (value)-variable, into the functions wherever self.x appears and calculates the answer.
            results.append(result)#adds the calculated answer the the end of the list "results"
        return results #returns the list (basically saves it) to be used if needed
    def eval_gradient(self, value): #this function will find the gradient of the functions at a given x value through diffing the function then subbing x
        gradients = [] #list to store the gradient answers
        for func in self.functions: #same as previous functions and the ones before that it was at this point that i recognised a pattern
            derivative = sp.diff(func, self.x) #derive each function (func) with respect to x (self.x) 
            gradient = derivative.subs(self.x, value) #for the previous answer (derivative) substitute the value we input for x (value) to get the gradient at that point which is stored as "gradient"
            gradients.append(gradient) #add the calculated gradient to the end of the list "gradients"
        return gradients #returns the list of gradients to be used if needed
    def eval_tangents(self, value):
        tangents = [] #list to store the tangent line equations
        for func in self.functions: #same as previous functions and the ones before that it was at this point that i recognised a pattern
            derivative = sp.diff(func, self.x) #derive each function (func) with respect to x (self.x) 
            gradient = derivative.subs(self.x, value) #for the previous answer (derivative) substitute the value we input for x (value) to get the gradient at that point which is stored as "gradient"
            y_value = func.subs(self.x, value) #calculate the y value at the given x value by substituting it into the original function
            tangent_line = gradient * (self.x - value) + y_value #using point-slope form to calculate the equation of the tangent line
            tangents.append(tangent_line) #add the calculated tangent line equation to the end of the list "tangents"
        return tangents #returns the list of tangent line equations to be used if needed
    def eval_xincpt(self):#solving for the x intercept of a function by making y = 0
        x_intcpt = [] #creating list to store solutions
        for func in self.functions:
            x_intercept = sp.solve(func, self.x) #passing func = x**2 for example automatically assumes its = 0 and hence solves for roots
            x_intcpt.append(x_intercept) #adds the calculated x intercepts to the end of the list "x_intcpt"
        return x_intcpt #returns the list of x intercepts to be used if needed
