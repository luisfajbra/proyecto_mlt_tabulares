import pandas as pd
import os

# Change to project directory
os.chdir(r"c:\Users\Luis\OneDrive - Universidad de los andes\SEMESTRES\Maestria\Machine learning techniques\proyecto")

df_train = pd.read_csv('Multimodal_CIC-MalDroid2020/Tabular/train-tabular.csv')
df_test = pd.read_csv('Multimodal_CIC-MalDroid2020/Tabular/test-tabular.csv')
df_adv = pd.read_csv('Multimodal_CIC-MalDroid2020/Tabular/adv-tabular.csv')
df_obfus = pd.read_csv('Multimodal_CIC-MalDroid2020/Tabular/obfus-tabular.csv')

print("=" * 70)
print("TRAIN DATA:")
print("=" * 70)
print(f"Shape: {df_train.shape}")
print(f"Number of features: {df_train.shape[1] - 2}")
print(f"\nFirst 10 columns:")
for col in df_train.columns.tolist()[:10]:
    print(f"  - {col}")
print(f"\nClass distribution:")
print(df_train['Class'].value_counts().sort_index())
print(f"Total null values: {df_train.isnull().sum().sum()}")
print(f"Data types: {df_train.dtypes.value_counts().to_dict()}")

print("\n" + "=" * 70)
print("TEST DATA:")
print("=" * 70)
print(f"Shape: {df_test.shape}")
print(f"Class distribution:")
print(df_test['Class'].value_counts().sort_index())

print("\n" + "=" * 70)
print("ADV DATA (ADVERSARIAL):")
print("=" * 70)
print(f"Shape: {df_adv.shape}")
print(f"Class distribution:")
print(df_adv['Class'].value_counts().sort_index())

print("\n" + "=" * 70)
print("OBFUS DATA (OBFUSCATED):")
print("=" * 70)
print(f"Shape: {df_obfus.shape}")
print(f"Class distribution:")
print(df_obfus['Class'].value_counts().sort_index())

print("\n" + "=" * 70)
print("COMBINED STATISTICS:")
print("=" * 70)
all_classes = pd.concat([df_train['Class'], df_test['Class']])
print(f"Total main dataset samples: {len(all_classes)}")
print(f"Combined class distribution:")
print(all_classes.value_counts().sort_index())

print("\n" + "=" * 70)
print("FEATURE CHARACTERISTICS:")
print("=" * 70)
# Take only feature columns (exclude apk_name and Class)
features = df_train.columns.tolist()[1:-1]
print(f"Number of features: {len(features)}")
print(f"\nSample features (first 15):")
for feat in features[:15]:
    print(f"  - {feat}")
