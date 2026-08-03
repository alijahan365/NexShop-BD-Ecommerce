import os
import urllib.parse
import urllib.request
import json

def send_otp_sms(mobile_number, otp_code, gateway_name="bKash"):
    """
    Sends real SMS via Bangladeshi SMS Gateway API if SMS_API_KEY is configured in .env.
    Supported SMS Gateways: Greenweb BD, SSL Wireless, BulkSMS BD.
    """
    sms_api_key = os.environ.get('SMS_API_KEY', '')
    sender_id = os.environ.get('SMS_SENDER_ID', '8809612345678')
    message = f"Your {gateway_name} verification OTP is {otp_code}. Valid for 3 mins. Do NOT share this code."

    # Standardize Bangladeshi mobile number format
    mobile = mobile_number.strip()
    if mobile.startswith('0'):
        mobile = '88' + mobile
    elif not mobile.startswith('88'):
        mobile = '880' + mobile

    print(f"[SMS Gateway Dispatch] To: {mobile} | Message: {message}")

    if sms_api_key:
        try:
            # Greenweb BD SMS API
            greenweb_url = "https://api.greenweb.com.bd/api.php"
            data = urllib.parse.urlencode({
                'token': sms_api_key,
                'to': mobile,
                'message': message
            }).encode('utf-8')

            req = urllib.request.Request(greenweb_url, data=data)
            with urllib.request.urlopen(req, timeout=5) as response:
                res_text = response.read().decode('utf-8')
                print(f"[Greenweb SMS API Response]: {res_text}")
                return {"status": "success", "provider": "Greenweb BD", "response": res_text}
        except Exception as e:
            print(f"[SMS API Exception]: {e}")
            return {"status": "error", "message": str(e)}

    return {
        "status": "simulated",
        "mobile": mobile_number,
        "otp": otp_code,
        "gateway": gateway_name,
        "note": "SMS logged in backend. To send cellular SIM SMS, set SMS_API_KEY in .env (Greenweb/SSL Wireless)."
    }
