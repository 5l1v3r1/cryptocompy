# get_coin_list.py
import json
import requests

def get_coin_list(coins='all'):
	"""
	Get general information about all the coins available on 
	cryptocompare.com.
	
	Args:
		coins: Default of 'all' returns complete list. Otherwise a list of coin
			symbols can be used.

	Returns:
		The function returns a dictionairy containing individual dictionairies 
		for the coins specified by the input. The key of the top dictionary 
		corresponds to the coin symbol. Each coin dictionary has the following 
		structure:
			{'Algorithm' : ...,
			 'CoinName': ...,
			 'FullName': ...,
			 'FullyPremined': ...,
			 'Id': ...,
			 'ImageUrl': ...,
			 'Name': ...,
			 'PreMinedValue': ...,
			 'ProofType': ...,
			 'SortOrder': ...,
			 'TotalCoinsFreeFloat': ...,
			 'TotalCoinSupply': ...,
			 'Url': ...}
	"""
	
	# http request
	url = "https://www.cryptocompare.com/api/data/coinlist/"
	r = requests.get(url)

	# data extraction
	data = r.json()
	
	message = data["Message"]
	data = data["Data"]

	print(message)

	# coins specified
	if coins != 'all':
		data = {c: data[c] for c in coins}

	return data


if __name__ == "__main__":

	print("Examples get_coin_list()")
	print("--------------------------------")
	coin_data = get_coin_list(["BTC", "ETH"])
	print(coin_data)
	print()

	coin_data = get_coin_list()
	print(list(coin_data.keys())[:10])
	print()