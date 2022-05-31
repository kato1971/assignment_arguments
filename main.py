# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# PART 1
def greet(name, greeting_template="Hello, <name>!"):
    greeting = greeting_template.replace('<name>', name)
    return greeting
print(greet("Kato"))
print(greet("Kato", "What's up, <name>!"))

# PART 2
def force(mass, body="earth"):
    gravity = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.2,
        "saturn" : 10.4,
        "earth" : 9.8,
        "uranus" : 8.9,
        "venus" : 8.9,
        "mars" : 3.7,
        "mercury" : 3.7,
        "moon" : 1.6,
        "pluto" : 0.6
    }
    F_gravity = mass * gravity[body]
    return F_gravity
print(force(10,"sun"))

def pull(m1, m2, d):
    G = 6.674 * 10 ** -11
    F = G * (m1 * m2) / d ** 2
    return F
print(pull(800, 1500, 3))


