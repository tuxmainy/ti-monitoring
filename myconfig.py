import os

# helper: convert string into boolean
def str_to_bool(value: str) -> bool:
    return value.lower() in ("1", "true", "yes", "on")

# URL for API
url = 'https://ti-lage.prod.ccs.gematik.solutions/lageapi/v1/tilage/bu/PU'

# path to hdf5 file for saving the availability data 
file_name = os.getenv('DATA_FILE', 'data.hdf5')

# switching email notofications on/off
notifications = str_to_bool(os.getenv('NOTIFY', 'False'))

# configuration for notofications
notifications_config_file = os.getenv('NOTIFY_CONF', 'notifications.json')

# smtp settings for email notifications
smtp_settings = {
    'host' : os.getenv('SMTP_USER', '********'),
    'port' : int(os.getenv('SMTP_PORT', '587')),
    'user' : os.getenv('SMTP_USER', '********'),
    'password' : os.getenv('SMTP_PASS', '********'),
    'from' : os.getenv('SMTP_FROM', '********')
}

# home url for dash app
home_url = os.getenv('BASE_URL', 'https://ti-monitoring.lukas-schmidt-russnak.de')

# time frame for statistics in web app
stats_delta_hours = 12

def main():
    return

if __name__ == '__main__':
    main()
