import tkinter as tk
from tkinter import ttk, messagebox
import requests

# --- Currency Data (ISO 4217 with country names) ---
currency_dict = {
    "AED": "United Arab Emirates Dirham (AED)",
    "AFN": "Afghan Afghani (AFN)",
    "ALL": "Albanian Lek (ALL)",
    "AMD": "Armenian Dram (AMD)",
    "ANG": "Netherlands Antillean Guilder (ANG)",
    "AOA": "Angolan Kwanza (AOA)",
    "ARS": "Argentine Peso (ARS)",
    "AUD": "Australian Dollar (AUD)",
    "AWG": "Aruban Florin (AWG)",
    "AZN": "Azerbaijani Manat (AZN)",
    "BAM": "Bosnia-Herzegovina Convertible Mark (BAM)",
    "BBD": "Barbadian Dollar (BBD)",
    "BDT": "Bangladeshi Taka (BDT)",
    "BGN": "Bulgarian Lev (BGN)",
    "BHD": "Bahraini Dinar (BHD)",
    "BIF": "Burundian Franc (BIF)",
    "BMD": "Bermudian Dollar (BMD)",
    "BND": "Brunei Dollar (BND)",
    "BOB": "Bolivian Boliviano (BOB)",
    "BRL": "Brazilian Real (BRL)",
    "BSD": "Bahamian Dollar (BSD)",
    "BTN": "Bhutanese Ngultrum (BTN)",
    "BWP": "Botswana Pula (BWP)",
    "BYN": "Belarusian Ruble (BYN)",
    "BZD": "Belize Dollar (BZD)",
    "CAD": "Canadian Dollar (CAD)",
    "CHF": "Swiss Franc (CHF)",
    "CLP": "Chilean Peso (CLP)",
    "CNY": "Chinese Yuan (CNY)",
    "COP": "Colombian Peso (COP)",
    "CRC": "Costa Rican Colón (CRC)",
    "CUP": "Cuban Peso (CUP)",
    "CVE": "Cape Verdean Escudo (CVE)",
    "CZK": "Czech Koruna (CZK)",
    "DJF": "Djiboutian Franc (DJF)",
    "DKK": "Danish Krone (DKK)",
    "DOP": "Dominican Peso (DOP)",
    "DZD": "Algerian Dinar (DZD)",
    "EGP": "Egyptian Pound (EGP)",
    "ERN": "Eritrean Nakfa (ERN)",
    "ETB": "Ethiopian Birr (ETB)",
    "EUR": "Euro (EUR)",
    "FJD": "Fijian Dollar (FJD)",
    "FKP": "Falkland Islands Pound (FKP)",
    "GBP": "British Pound (GBP)",
    "GEL": "Georgian Lari (GEL)",
    "GHS": "Ghanaian Cedi (GHS)",
    "GIP": "Gibraltar Pound (GIP)",
    "GMD": "Gambian Dalasi (GMD)",
    "GNF": "Guinean Franc (GNF)",
    "GTQ": "Guatemalan Quetzal (GTQ)",
    "GYD": "Guyanese Dollar (GYD)",
    "HKD": "Hong Kong Dollar (HKD)",
    "HNL": "Honduran Lempira (HNL)",
    "HRK": "Croatian Kuna (HRK)",
    "HTG": "Haitian Gourde (HTG)",
    "HUF": "Hungarian Forint (HUF)",
    "IDR": "Indonesian Rupiah (IDR)",
    "ILS": "Israeli New Shekel (ILS)",
    "INR": "Indian Rupee (INR)",
    "IQD": "Iraqi Dinar (IQD)",
    "IRR": "Iranian Rial (IRR)",
    "ISK": "Icelandic Krona (ISK)",
    "JMD": "Jamaican Dollar (JMD)",
    "JOD": "Jordanian Dinar (JOD)",
    "JPY": "Japanese Yen (JPY)",
    "KES": "Kenyan Shilling (KES)",
    "KGS": "Kyrgyzstani Som (KGS)",
    "KHR": "Cambodian Riel (KHR)",
    "KMF": "Comorian Franc (KMF)",
    "KRW": "South Korean Won (KRW)",
    "KWD": "Kuwaiti Dinar (KWD)",
    "KYD": "Cayman Islands Dollar (KYD)",
    "KZT": "Kazakhstani Tenge (KZT)",
    "LAK": "Lao Kip (LAK)",
    "LBP": "Lebanese Pound (LBP)",
    "LKR": "Sri Lankan Rupee (LKR)",
    "LRD": "Liberian Dollar (LRD)",
    "LSL": "Lesotho Loti (LSL)",
    "LYD": "Libyan Dinar (LYD)",
    "MAD": "Moroccan Dirham (MAD)",
    "MDL": "Moldovan Leu (MDL)",
    "MGA": "Malagasy Ariary (MGA)",
    "MKD": "Macedonian Denar (MKD)",
    "MMK": "Burmese Kyat (MMK)",
    "MNT": "Mongolian Tugrik (MNT)",
    "MOP": "Macanese Pataca (MOP)",
    "MRU": "Mauritanian Ouguiya (MRU)",
    "MUR": "Mauritian Rupee (MUR)",
    "MVR": "Maldivian Rufiyaa (MVR)",
    "MWK": "Malawian Kwacha (MWK)",
    "MXN": "Mexican Peso (MXN)",
    "MYR": "Malaysian Ringgit (MYR)",
    "MZN": "Mozambican Metical (MZN)",
    "NAD": "Namibian Dollar (NAD)",
    "NGN": "Nigerian Naira (NGN)",
    "NIO": "Nicaraguan Córdoba (NIO)",
    "NOK": "Norwegian Krone (NOK)",
    "NPR": "Nepalese Rupee (NPR)",
    "NZD": "New Zealand Dollar (NZD)",
    "OMR": "Omani Rial (OMR)",
    "PAB": "Panamanian Balboa (PAB)",
    "PEN": "Peruvian Sol (PEN)",
    "PGK": "Papua New Guinean Kina (PGK)",
    "PHP": "Philippine Peso (PHP)",
    "PKR": "Pakistani Rupee (PKR)",
    "PLN": "Polish Zloty (PLN)",
    "PYG": "Paraguayan Guarani (PYG)",
    "QAR": "Qatari Rial (QAR)",
    "RON": "Romanian Leu (RON)",
    "RSD": "Serbian Dinar (RSD)",
    "RUB": "Russian Ruble (RUB)",
    "RWF": "Rwandan Franc (RWF)",
    "SAR": "Saudi Riyal (SAR)",
    "SBD": "Solomon Islands Dollar (SBD)",
    "SCR": "Seychellois Rupee (SCR)",
    "SDG": "Sudanese Pound (SDG)",
    "SEK": "Swedish Krona (SEK)",
    "SGD": "Singapore Dollar (SGD)",
    "SHP": "Saint Helena Pound (SHP)",
    "SLL": "Sierra Leonean Leone (SLL)",
    "SOS": "Somali Shilling (SOS)",
    "SRD": "Surinamese Dollar (SRD)",
    "SSP": "South Sudanese Pound (SSP)",
    "STN": "São Tomé and Príncipe Dobra (STN)",
    "SYP": "Syrian Pound (SYP)",
    "SZL": "Swazi Lilangeni (SZL)",
    "THB": "Thai Baht (THB)",
    "TJS": "Tajikistani Somoni (TJS)",
    "TMT": "Turkmenistani Manat (TMT)",
    "TND": "Tunisian Dinar (TND)",
    "TOP": "Tongan Paʻanga (TOP)",
    "TRY": "Turkish Lira (TRY)",
    "TTD": "Trinidad and Tobago Dollar (TTD)",
    "TWD": "New Taiwan Dollar (TWD)",
    "TZS": "Tanzanian Shilling (TZS)",
    "UAH": "Ukrainian Hryvnia (UAH)",
    "UGX": "Ugandan Shilling (UGX)",
    "USD": "United States Dollar (USD)",
    "UYU": "Uruguayan Peso (UYU)",
    "UZS": "Uzbekistani Som (UZS)",
    "VES": "Venezuelan Bolívar (VES)",
    "VND": "Vietnamese Dong (VND)",
    "VUV": "Vanuatu Vatu (VUV)",
    "WST": "Samoan Tala (WST)",
    "XAF": "Central African CFA Franc (XAF)",
    "XCD": "East Caribbean Dollar (XCD)",
    "XOF": "West African CFA Franc (XOF)",
    "XPF": "CFP Franc (XPF)",
    "YER": "Yemeni Rial (YER)",
    "ZAR": "South African Rand (ZAR)",
    "ZMW": "Zambian Kwacha (ZMW)",
    "ZWL": "Zimbabwean Dollar (ZWL)"
}

# --- API Fallback ---
def fetch_rates(base="USD"):
    urls = [
        f"https://open.er-api.com/v6/latest/{base}",
        f"https://api.exchangerate.host/latest?base={base}"
    ]
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if "rates" in data:
                    return data["rates"]
                elif "result" in data and data["result"] == "success":
                    return data["rates"]
        except Exception:
            continue
    messagebox.showerror("Error", "Unable to fetch live rates. Please check internet.")
    return None

# --- Conversion Function ---
def convert():
    amount = entry_amount.get()
    if not amount:
        messagebox.showwarning("Input Error", "Please enter an amount")
        return
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid amount")
        return

    from_currency = combo_from.get().split("(")[-1][:-1]
    to_currency = combo_to.get().split("(")[-1][:-1]

    rates = fetch_rates(from_currency)
    if rates and to_currency in rates:
        converted_amount = amount * rates[to_currency]
        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        messagebox.showerror("Error", "Conversion failed. Try again later.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.configure(bg="#f0f4f7")

style = ttk.Style(root)
style.theme_use("clam")

label_title = tk.Label(root, text="💱 Currency Converter", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333")
label_title.pack(pady=20)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

label_amount = tk.Label(frame, text="Amount:", font=("Arial", 12), bg="#02090f")
label_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(frame, font=("Arial", 12))
entry_amount.grid(row=0, column=1, padx=5, pady=5)

label_from = tk.Label(frame, text="From:", font=("Arial", 12), bg="#02090f")
label_from.grid(row=1, column=0, padx=5, pady=5)

combo_from = ttk.Combobox(frame, values=sorted(currency_dict.values()), font=("Arial", 11), width=30)
combo_from.grid(row=1, column=1, padx=5, pady=5)
combo_from.set("United States Dollar (USD)")

label_to = tk.Label(frame, text="To:", font=("Arial", 12), bg="#02090f")
label_to.grid(row=2, column=0, padx=5, pady=5)

combo_to = ttk.Combobox(frame, values=sorted(currency_dict.values()), font=("Arial", 11), width=30)
combo_to.grid(row=2, column=1, padx=5, pady=5)
combo_to.set("Indian Rupee (INR)")

convert_btn = tk.Button(root, text="Convert", command=convert, font=("Arial", 14, "bold"), bg="#4caf50", fg="white", relief="flat", padx=20, pady=10)
convert_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f4f7", fg="#222")
result_label.pack(pady=20)

root.mainloop()