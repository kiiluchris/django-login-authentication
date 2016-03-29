from authomatic.providers import oauth2, oauth1, openid

CONFIG = {
	# Twitter
	'tw':{
		# Class
		'class_': oauth1.Twitter,

		# Authorization
		'consumer_key': '83yaVqGFQeAT8v0PV8afL5jMj',
		'consumer_secret': '7VaxA43PEYh2xB9rZxW4ZogRkrk120qUn4XNjVQGFtnBeH4VB0',
	},
	# Facebook
	'fb':{
		'class_': oauth2.Facebook,

		# Authorization
		'consumer_key': '1720637118212458',
		'consumer_secret': '4a4406bbba4a977e6eee28f9e8f27103',

		# Scop of oauth2

		'scope': ['user_about_me', 'email', 'publish_stream'],
	},

	# Open Id
	'oi':{
		'class_': openid.OpenID,
	},
}