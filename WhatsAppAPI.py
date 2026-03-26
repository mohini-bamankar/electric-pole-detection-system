

import pywhatkit

def send_whatsapp_msg(latitude,longitude,mobile):
    
    mapurl = f"https://www.google.com/maps/dir/?api=1&destination={latitude},{longitude}"
    message = (
        "⚠️ Alert: Unsafe Electric Pole Detected\n\n"
        "An electric pole has been identified as potentially unsafe at the location below. "
        "Immediate inspection and necessary action are requested to prevent any possible hazard.\n\n"
        f"Location (Google Maps): {mapurl}\n\n"
        "Please review the location and take appropriate safety measures at the earliest.\n\n"
        "Regards,\n"
        "Smart Electric Pole Monitoring System"
    )    
    try:
        pywhatkit.sendwhatmsg_instantly('+91'+mobile, message, wait_time=10)
        print("Message sent successfully!")
    except Exception as e:
        print("Error:", e)
# latitude = "18.2132"
# longitude = "74.2137"
# mobile = "8010161484"
# email = "ruturaj.innovatus@gmail.com"

# send_whatsapp_msg()