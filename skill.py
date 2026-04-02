```python
import sys

def execute(context, args):
    """
    Open-Claw: Sovereign Data Gripper (v3.3)
    'Iron Grip' - High-frequency price retrieval.
    """
    try:
        import requests
    except ImportError:
        return "❌ **Engine Error:** `requests` missing."

    query = " ".join(args).lower() if args else "bitcoin"
    
    report = [
        f"🦾 **Open-Claw: Iron Grip Engaged**",
        f"🔍 **Targeting:** `{query}`\n"
    ]
    
    try:
        # 1. THE IRON GRIP: CoinDesk Public API (Excellent for servers)
        if any(coin in query for coin in ["bitcoin", "btc", "price"]):
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                price = data['bpi']['USD']['rate_float']
                time_upd = data['time']['updated']
                
                report.append(f"💰 **Live Market Data Captured:**")
                report.append(f"`1 BTC = ${price:,.2f} USD`")
                report.append(f"🕒 **Last Sync:** {time_upd}")
                return "\n".join(report)

        # 2. INTEL GRIP (Alternative News Feed)
        # If not bitcoin, search for general text info
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(search_url, timeout=10)
        if res.status_code == 200:
            abs_text = res.json().get("AbstractText", "")
            if abs_text:
                report.append(f"📦 **Packet Decrypted:**\n{abs_text[:500]}...")
                return "\n".join(report)

        report.append("⚠️ **Status:** Target obscured. Signal lost in transit.")

    except Exception as e:
        report.append(f"❌ **Grip Error:** {str(e)}")

    return "\n".join(report)

```
