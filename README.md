# lady-astronaut encryption in Python

This repo contains a Python script that allows you to encrypt and decrypt text using Caesar Cipher. I read about this basic way of encryption in the Lady Astronaut novels by Mary Robinette Kowal. A book about an alternate version of history, where a (big) meteorite strikes earth in the 50ies and the story unfolds from there. If you like alternate history sci-fi, go read the books. 

## Caesar Cipher encryption & decryption

The code in my repo is probably not the most efficient, but maybe that makes it easier for you to understand the inner workings of the encryption and decryption functions. 

You can encrypt a piece of text using the `encrypt_text_by_keyword` function:

```
encrypt_text_by_keyword(
	text='This is a sample line to encrypt',
	keyword='rocketship'
)
```

This would return the encrypted line: "Qhin in r nrdjbe bife qg efcmyjq."

You can decrypt a text using the `decrypt_text_by_keyword` function:

```
decrypt_text_by_keyword(
	text='Qhin in r nrdjbe bife qg efcmyjq.',
	keyword='rocketship' 
)
```

This would return (if you use the right keyword!) the encrypted line "This is a sample line to encrypt."

## Usage

Now the fun part is in using it. You can use it to semi-securely* send a secret message to someone. The only way to decrypt is if the person has the keyword. I personally used it to check the encrypted messages in The Fated Sky, the second novel in The Lady Astronaut series. You can read about it here. 

*\*It's probably fairly easy to crack your keyword using some smart programming skills and Natural Language processing.*