import joblib
import json

def encodeInput(ip):
    # ip = json.loads(ipjson)
    scaler = joblib.load("./helper/scaler.pkl")
    label_encoder = joblib.load('./helper/label_encoders.pkl')

    ip_encoded = []
    for feature, value in ip.items():
        if feature in label_encoder:
            ip_encoded.append(label_encoder[feature].transform([value])[0])
        else:
            ip_encoded.append(value)
    ip_encoded[0] = scaler.transform([[ip_encoded[0]]])[0]
    ip_encoded[0] = ip_encoded[0][0]

    return ip_encoded