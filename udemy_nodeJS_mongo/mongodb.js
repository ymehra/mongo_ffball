// crud operations
//create, read, update and delete opertations

const mongodb = require('mongodb')
const MongoClient = mongodb.MongoClient

const uri = 'mongodb+srv://yashmehra73:wic-eawn-FEAD9vis@ffball.baakg.mongodb.net/ffball?retryWrites=true&w=majority'
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true })
const databaseName = 'ffball'

client.connect((err, client) => {
	if (err) {
		return console.log('Unable to connect to database!')
	}
	const db = client.db(databaseName)
	db.collection('users').insertOne({
		name : 'Yash',
		age  : 25
	})
})
