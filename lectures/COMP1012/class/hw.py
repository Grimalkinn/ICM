### etox
import math

def etox(x, tolerance):
    """
    Computes an approximation to e^x using a series expansion. 

    Args:
        x: The exponent value (float). 
        tolerance: The minimum absolute value for a term to be included (float). 

    Returns:
        A tuple containing the approximate value of e^x and the number of terms summed. 
    """
    total_sum = 0.0
    term = 1.0  # First term of the series (x^0 / 0!)
    n = 0
    count = 0

    while abs(term) > tolerance: #[cite: 26]
        total_sum += term
        count += 1
        n += 1
        # Calculate the next term based on the previous one to avoid factorial calculation
        # term_n = term_(n-1) * x / n
        if n > 0:
            term = term * x / n
        else: # Should only happen after the first term where n becomes 1
             term = term * x
             
    return total_sum, count #[cite: 27]
### etox

###compute trajectory
def computeTrajectory(a, b, c, distance, intervals):
    """
    Computes the X and Y coordinates for a projectile's trajectory. 

    Args:
        a, b, c: Coefficients of the quadratic equation y(x) = ax^2 + bx + c. 
        distance: The total horizontal distance the projectile travels. 
        intervals: The number of equal-width intervals along the x-axis. 

    Returns:
        A tuple containing the list of X coordinates and the list of Y coordinates. 
    """
    x_coords = [] #[cite: 31]
    y_coords = [] #[cite: 32]

    if intervals > 0:
        delta_x = distance / intervals
        for i in range(intervals + 1):
            x = i * delta_x
            y = a * x**2 + b * x + c
            x_coords.append(x) #[cite: 31]
            y_coords.append(y) #[cite: 32]
            
    return x_coords, y_coords #[cite: 33]
###compute trajectory

###main
import math

# --- Assume the computeTrajectory function from question 17 is defined here ---
def computeTrajectory(a, b, c, distance, intervals):
    x_coords = []
    y_coords = []
    if intervals > 0:
        delta_x = distance / intervals
        for i in range(intervals + 1):
            x = i * delta_x
            y = a * x**2 + b * x + c
            x_coords.append(x)
            y_coords.append(y)
    return x_coords, y_coords
# -------------------------------------------------------------------------

def main():
    # Constants
    G = 9.81
    v0 = 25.25
    y0 = 2.1

    while True:
        # Input the number of intervals
        intervals_str = input("Enter the number of intervals (<=0 to quit): ") #[cite: 46]
        intervals = int(intervals_str)

        # Loop as long as the number of intervals is greater than zero
        if intervals <= 0: ##[cite: 37]
            break

        # Input the launch angle
        angle_str = input("Enter the launch angle of the projectile (> 0): ") #[cite: 38]
        launch_angle_deg = float(angle_str)

        # Validate the launch angle
        if launch_angle_deg <= 0: ##[cite: 39]
            print(f"The launch angle, {launch_angle_deg:.1f}, must be greater than zero!") #[cite: 39]
            print()
            continue

        # Convert angle to radians for math functions
        theta_rad = math.radians(launch_angle_deg)

        # Compute coefficients a, b, c and distance
        a = -G / (2 * v0**2 * math.cos(theta_rad)**2) #[cite: 40]
        b = math.tan(theta_rad) #[cite: 40]
        c = y0 #[cite: 41]
        
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            distance = 0 # Or handle as an error
        else:
            distance = (-b - math.sqrt(discriminant)) / (2 * a) #[cite: 41]

        # Get the lists of X and Y coordinates
        x_points, y_points = computeTrajectory(a, b, c, distance, intervals) #[cite: 42]

        # Display the heading and results
        print()
        print("X coordinate Y coordinate") #[cite: 43]
        for i in range(len(x_points)): #[cite: 44]
            # Display coordinates to 4 decimal places in 12 character positions
            print(f"{x_points[i]:12.4f}{y_points[i]:12.4f}") #[cite: 44, 47]
        print()

# Run the main program
if __name__ == "__main__":
    main()
###main

