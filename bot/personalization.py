from .utils import load_user_profile, save_user_profile

def set_user_name(name):
    profile = load_user_profile()
    profile["name"] = name
    save_user_profile(profile)

def set_weather_unit(unit):
    profile = load_user_profile()
    profile["preferences"]["weather_unit"] = unit
    save_user_profile(profile)

def get_user_name():
    profile = load_user_profile()
    return profile.get("name", "User")

def get_weather_unit():
    profile = load_user_profile()
    #return profile["preferences"].get("weather_unit", "Celsius")
    return profile["preferences"].get("weather_unit", "metric")
