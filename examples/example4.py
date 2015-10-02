import trade

# create some assets
asset = trade.Asset(name='some asset')
other_asset = trade.Asset(name='other asset')

# create the purchase operation buying 10 stocks
purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=10,
                date='2015-10-01'
            )
# create another purchase operation, again buying 10 stocks,
# but with a different price
other_purchase = trade.Operation(
                asset=asset,
                quantity=10,
                price=20,
                date='2015-10-01'
            )
# create a purchase operation buying 10 stocks
# of some other asset
other_asset_purchase = trade.Operation(
                asset=other_asset,
                quantity=10,
                price=10,
                date='2015-10-01'
            )

# Create the operation container
container = trade.OperationContainer()

# Append all operations on the OperationContainer
# operations attribute, which is a list.
container.operations.append(purchase)
container.operations.append(other_purchase)
container.operations.append(other_asset_purchase)

# Run the container default method to fetch the positions
# resulting from this opeations:
container.fetch_positions()

# Check the raw container positions
print(container.positions)

# Check each position
print(container.positions['common operations'][asset].asset.name)
print(container.positions['common operations'][asset].quantity)
print(container.positions['common operations'][asset].price)

print(container.positions['common operations'][other_asset].asset.name)
print(container.positions['common operations'][other_asset].quantity)
print(container.positions['common operations'][other_asset].price)
