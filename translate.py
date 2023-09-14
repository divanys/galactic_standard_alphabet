import galactic_alph, to_pictures

input_str = input("Введите фразу на английском: ").lower()
cleaned_str = ''.join(c for c in input_str if c in galactic_alph.alphabet_en)

galactic_array = []

for c in cleaned_str:
    galactic_array.append(galactic_alph.alphabet_of_galactic[galactic_alph.alphabet_en.index(c)])

# print(galactic_array)
to_pictures.to_pictures(galactic_array)

