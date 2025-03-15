# The Vigenère Cipher

# Шифр Виженера

## 📜 Описание

Шифр Виженера — это метод полиалфавитного шифрования, который используется для защиты текстовой информации. Он был разработан Блезом Виженером в 1586 году и является более сложным вариантом шифра Цезаря. Главное преимущество заключается в возможности выбора произвольного алфавита и ключа, что делает шифрование более безопасным.

## 🔑 Принцип работы

### 1. Подготовка данных

- **Символы**: Шифр Виженера может работать с любыми символами, включая буквы, цифры и специальные символы. Для этого необходимо определить свой собственный алфавит.
- **Удаление пробелов**: Входной текст может быть очищен от пробелов и других нежелательных символов, если это необходимо.

### 2. Определение алфавита

- **Алфавит**: Пользователь может самостоятельно задать алфавит, например, `ABCDEFGHIJKLMNOPQRSTUVWXYZ`, `0123456789`, или любой другой набор символов. Важно, чтобы все символы были уникальными.

  Пример:
  ```
  Алфавит: ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ```

### 3. Определение ключа

- **Ключ**: Ключ — это строка, используемая для шифрования текста. Он также может состоять из любых символов из заданного алфавита. Если длина ключа меньше длины текста, ключ повторяется до тех пор, пока не достигнет длины текста.

### 4. Шифрование текста

Шифрование текста происходит следующим образом:

1. **Создание таблицы соответствий**: На основе заданного алфавита создается таблица, где строки и столбцы соответствуют символам алфавита.

2. **Шифрование**:
   - Для каждого символа исходного текста (соответствующей позиции) и символа ключа определяется их позиция в алфавите.
   - Новый символ получается путем добавления позиций, учитывая размер алфавита:

   $$
   P_{\text{cipher}} = (P_T + P_K) \mod N
   $$

где:
- \( N \) — количество символов в алфавите
- \( P_T \) — позиция символа текста
- \( P_K \) — позиция символа ключа.

### 5. Расшифрование текста

Для расшифрования используется тот же ключ:

- Для каждого символа зашифрованного текста применяют следующую формулу:

$$
P_{\text{plain}} = (P_{\text{cipher}} - P_K + N) \mod N
$$

где:

- $P_{\text{plain}}$ — позиция символа в исходном тексте.
- $P_{\text{cipher}}$ — позиция символа в зашифрованном тексте.
- $P_K$ — позиция символа ключа.
- $N$ — количество символов в алфавите.

### 6. Пример шифрования и расшифрования

**Исходный текст**: `HELLO`
**Ключ**: `KEY`
**Алфавит**: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

1. Подготовка ключа: `KEYKE` (дополняем ключ до длины текста).
2. Зашифрование:
   - H (7) + K (10) = R (17)
   - E (4) + E (4) = I (8)
   - L (11) + Y (24) = J (9)
   - L (11) + K (10) = V (21)
   - O (14) + E (4) = S (18)

**Зашифрованный текст**: `RIJVS`

3. Расшифрование выполняется аналогично с использованием ключа `KEYKE`.

## 🔒 Заключение

Шифр Виженера позволяет пользователю задавать свой собственный алфавит и ключ, что делает его гибким инструментом для шифрования текста. Но, как и любой другой шифр, он подвержен атакам, поэтому важно использовать длину ключа, достаточную для обеспечения безопасности.

## 🔍 Почему стоит использовать шифр Виженера?

Шифр Виженера — это классический метод шифрования, который до сих пор вызывает интерес благодаря своей простоте и гибкости. Он позволяет пользователю настроить алфавит и ключ, что делает его уникальным для каждого случая использования. Хотя современные методы шифрования могут быть более надежными, шифр Виженера остается отличным учебным инструментом и может быть использован для базовой защиты данных.

## 🛠️ Как начать?

Если вы хотите попробовать шифр Виженера в действии, вы можете использовать различные онлайн-инструменты или написать собственный код на любом языке программирования. Это отличный способ понять основы криптографии и научиться защищать свои данные!
