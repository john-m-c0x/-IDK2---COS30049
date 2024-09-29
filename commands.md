# List Available Datasets and Features
- `python visualisation.py --list_datasets`

# Highest Regression Score
- `python visualisation.py -d set2 --highest_regression`
- `python visualisation.py -d set2 --highest_regression`

# Run Regression Analysis on Dataset 1 (set1)
- `python visualisation.py -d set1 -m regression -x ph -y Potability`
- `python visualisation.py -d set1 -m regression -x Hardness -y Potability`
- `python visualisation.py -d set1 -m regression -x Solids -y Potability`
- `python visualisation.py -d set1 -m regression -x Chloramines -y Potability`
- `python visualisation.py -d set1 -m regression -x Sulfate -y Potability`
- `python visualisation.py -d set1 -m regression -x Conductivity -y Potability`
- `python visualisation.py -d set1 -m regression -x Organic_carbon -y Potability`
- `python visualisation.py -d set1 -m regression -x Trihalomethanes -y Potability`
- `python visualisation.py -d set1 -m regression -x Turbidity -y Potability`

# Run Classification Analysis on Dataset 1 (set1)
- `python visualisation.py -d set1 -m classification -x Turbidity -y Potability`

# Visualize Data on Dataset 1 (set1)
- `python visualisation.py -d set1 -p scatter -x pH -y Hardness`
- `python visualisation.py -d set1 -p box -x Conductivity -y Potability`
- `python visualisation.py -d set1 -p histogram -x Chloramines`

# Run Regression Analysis on Dataset 2 (set2)
- `python visualisation.py -d set2 -m regression -x aluminium -y is_safe`
- `python visualisation.py -d set2 -m regression -x ammonia -y is_safe`
- `python visualisation.py -d set2 -m regression -x arsenic -y is_safe`
- `python visualisation.py -d set2 -m regression -x barium -y is_safe`
- `python visualisation.py -d set2 -m regression -x cadmium -y is_safe`
- `python visualisation.py -d set2 -m regression -x chloramine -y is_safe`
- `python visualisation.py -d set2 -m regression -x chromium -y is_safe`
- `python visualisation.py -d set2 -m regression -x copper -y is_safe`
- `python visualisation.py -d set2 -m regression -x flouride -y is_safe`
- `python visualisation.py -d set2 -m regression -x bacteria -y is_safe`
- `python visualisation.py -d set2 -m regression -x viruses -y is_safe`
- `python visualisation.py -d set2 -m regression -x lead -y is_safe`
- `python visualisation.py -d set2 -m regression -x nitrates -y is_safe`
- `python visualisation.py -d set2 -m regression -x nitrites -y is_safe`
- `python visualisation.py -d set2 -m regression -x mercury -y is_safe`
- `python visualisation.py -d set2 -m regression -x perchlorate -y is_safe`
- `python visualisation.py -d set2 -m regression -x radium -y is_safe`
- `python visualisation.py -d set2 -m regression -x selenium -y is_safe`
- `python visualisation.py -d set2 -m regression -x silver -y is_safe`
- `python visualisation.py -d set2 -m regression -x uranium -y is_safe`

# Run Classification Analysis on Dataset 2 (set2)
- `python visualisation.py -d set2 -m classification -x Arsenic -y is_safe`

# Visualize Data on Dataset 2 (set2)
- `python visualisation.py -d set2 -p scatter -x Hardness -y is_safe`
- `python visualisation.py -d set2 -p box -x Conductivity -y is_safe`
- `python visualisation.py -d set2 -p histogram -x Nitrates`

# Run Regression Analysis on Dataset 3 (set3)
- `python visualisation.py -d set3 -m regression -x Temperature -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x D.O -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x pH -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x Conductivity -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x B.O.D -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x Nitrate -y Totalcaliform`
- `python visualisation.py -d set3 -m regression -x Fecalcaliform -y Totalcaliform`

# Run Classification Analysis on Dataset 3 (set3)
- `python visualisation.py -d set3 -m classification -x [Your_Classification_Variable] -y Totalcaliform` 

