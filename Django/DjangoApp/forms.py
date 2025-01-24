from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Category, Post, Comment

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control mb-3'})
    )
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'})
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birthdate', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'icon', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'icon': forms.Select(
                choices=[
                    ('airplane-fill', 'Airplane'),
                    ('alarm-fill', 'Alarm'),
                    ('award-fill', 'Award'),
                    ('backpack-fill', 'Backpack'),
                    ('bag-fill', 'Bag'),
                    ('balloon-fill', 'Balloon'),
                    ('bandaid-fill', 'Bandaid'),
                    ('bank2', 'Bank'),
                    ('basket2-fill', 'Basket'),
                    ('battery-half', 'Battery'),
                    ('bell-fill', 'Bell'),
                    ('bicycle', 'Bicycle'),
                    ('binoculars-fill', 'Binoculars'),
                    ('book-half', 'Book'),
                    ('boombox-fill', 'Boombox'),
                    ('box-seam-fill', 'Box'),
                    ('bricks', 'Bricks'),
                    ('briefcase-fill', 'Briefcase'),
                    ('brilliance', 'Brilliance'),
                    ('broadcast-pin', 'Broadcast'),
                    ('brush-fill', 'Brush'),
                    ('bucket-fill', 'Bucket'),
                    ('bug-fill', 'Bug'),
                    ('buildings-fill', 'Buildings'),
                    ('bus-front-fill', 'Bus'),
                    ('cake2-fill', 'Cake'),
                    ('calculator', 'Calculator'),
                    ('calendar-week-fill', 'Calendar'),
                    ('camera-fill', 'Camera'),
                    ('capsule', 'Capsule'),
                    ('car-front-fill', 'Car'),
                    ('cart-fill', 'Cart'),
                    ('cash-stack', 'Cash'),
                    ('cassette-fill', 'Cassette'),
                    ('chat-left-text-fill', 'Chat'),
                    ('cloudy-fill', 'Clouds'),
                    ('code-slash', 'Code'),
                    ('coin', 'Coin'),
                    ('compass-fill', 'Compass'),
                    ('cone-striped', 'Cone'),
                    ('controller', 'Controller'),
                    ('cookie', 'Cookie'),
                    ('cpu-fill', 'CPU'),
                    ('crosshair2', 'Crosshair'),
                    ('cup-hot-fill', 'Cup'),
                    ('currency-exchange', 'Currency'),
                    ('dice-5-fill', 'Dice'),
                    ('display', 'Display'),
                    ('door-open-fill', 'Door'),
                    ('droplet-fill', 'Droplet'),
                    ('duffle-fill', 'Duffle'),
                    ('ear-fill', 'Ear'),
                    ('earbuds', 'Earbuds'),
                    ('easel2-fill', 'Easel'),
                    ('egg-fill', 'Egg'),
                    ('envelope-fill', 'Envelope'),
                    ('eraser-fill', 'Eraser'),
                    ('eye', 'Eye'),
                    ('eyedropper', 'Eyedropper'),
                    ('eyeglasses', 'Eyeglasses'),
                    ('fan', 'Fan'),
                    ('feather', 'Feather'),
                    ('film', 'Film'),
                    ('fingerprint', 'Fingerprint'),
                    ('fire', 'Fire'),
                    ('flag-fill', 'Flag'),
                    ('floppy2-fill', 'Floppy'),
                    ('flower2', 'Flower'),
                    ('gear-wide-connected', 'Gear'),
                    ('gem', 'Gem'),
                    ('geo-alt-fill', 'Geo'),
                    ('gift-fill', 'Gift'),
                    ('globe-americas', 'Globe'),
                    ('hammer', 'Hammer'),
                    ('handbag-fill', 'Handbag'),
                    ('headset', 'Headset'),
                    ('heart-fill', 'Heart'),
                    ('highlighter', 'Highlighter'),
                    ('hourglass-split', 'Hourglass'),
                    ('house-fill', 'House'),
                    ('image-fill', 'Image'),
                    ('incognito', 'Incognito'),
                    ('joystick', 'Joystick'),
                    ('key-fill', 'Key'),
                    ('keyboard-fill', 'Keyboard'),
                    ('ladder', 'Ladder'),
                    ('lamp-fill', 'Lamp'),
                    ('laptop', 'Laptop'),
                    ('lightbulb-fill', 'Lightbulb'),
                    ('lightning-fill', 'Lightning'),
                    ('lock-fill', 'Lock'),
                    ('luggage-fill', 'Luggage'),
                    ('lungs-fill', 'Lungs'),
                    ('magic', 'Magic'),
                    ('magnet-fill', 'Magnet'),
                    ('mailbox2-flag', 'Mailbox'),
                    ('map-fill', 'Map'),
                    ('megaphone-fill', 'Megaphone'),
                    ('mic-fill', 'Mic'),
                    ('minecart-loaded', 'Minecart'),
                    ('modem-fill', 'Modem'),
                    ('moon-fill', 'Moon'),
                    ('mortarboard-fill', 'Mortarboard'),
                    ('motherboard-fill', 'Motherboard'),
                    ('mouse2-fill', 'Mouse'),
                    ('music-note-beamed', 'Music'),
                    ('newspaper', 'Newspaper'),
                    ('nut-fill', 'Nut'),
                    ('paint-bucket', 'Paint'),
                    ('palette-fill', 'Palette'),
                    ('paperclip', 'Paperclip'),
                    ('paragraph', 'Paragraph'),
                    ('pass-fill', 'Pass'),
                    ('passport-fill', 'Passport'),
                    ('pc-display', 'PC'),
                    ('peace', 'Peace'),
                    ('pen-fill', 'Pen'),
                    ('pencil-fill', 'Pencil'),
                    ('people-fill', 'People'),
                    ('person-fill', 'Person'),
                    ('percent', 'Percent'),
                    ('phone-fill', 'Phone'),
                    ('piggy-bank-fill', 'Piggy'),
                    ('pin-angle-fill', 'Pin'),
                    ('plug-fill', 'Plug'),
                    ('postage-fill', 'Postage'),
                    ('postcard-fill', 'Postcard'),
                    ('power', 'Power'),
                    ('printer-fill', 'Printer'),
                    ('projector-fill', 'Projector'),
                    ('puzzle-fill', 'Puzzle'),
                    ('qr-code', 'QR-code'),
                    ('radar', 'Radar'),
                    ('radioactive', 'Rradioactive'),
                    ('rainbow', 'Rainbow'),
                    ('receipt', 'Receipt'),
                    ('robot', 'Robot'),
                    ('rocket-takeoff-fill', 'Rocket'),
                    ('router-fill', 'Router'),
                    ('rulers', 'Rulers'),
                    ('safe-fill', 'Safe'),
                    ('scissors', 'Scissors'),
                    ('scooter', 'Scooter'),
                    ('screwdriver', 'Screwdriver'),
                    ('sd-card-fill', 'SD-card'),
                    ('search', 'Search'),
                    ('send-fill', 'Send'),
                    ('server', 'Server'),
                    ('share-fill', 'Share'),
                    ('shield-shaded', 'Shiels'),
                    ('shop-window', 'Shop'),
                    ('signpost-2-fill', 'Signpost'),
                    ('sim-fill', 'SIM'),
                    ('smartwatch', 'Smartwatch'),
                    ('snow', 'Snow'),
                    ('speaker-fill', 'Speaker'),
                    ('speedometer', 'Speedometer'),
                    ('star-half', 'Star'),
                    ('stoplights-fill', 'Stoplights'),
                    ('stopwatch-fill', 'Stopwatch'),
                    ('suitcase2-fill', 'Suitcase'),
                    ('sun-fill', 'Sun'),
                    ('sunglasses', 'Sunglasses'),
                    ('table', 'Table'),
                    ('tablet-landscape-fill', 'Tablet'),
                    ('tag-fill', 'Tag'),
                    ('taxi-front-fill', 'Taxi'),
                    ('telephone-fill', 'Telephone'),
                    ('thermometer-half', 'Thermometer'),
                    ('ticket-perforated-fill', 'Ticket'),
                    ('tools', 'Tools'),
                    ('tornado', 'Tornado'),
                    ('train-front-fill', 'Train'),
                    ('translate', 'Translate'),
                    ('trash3-fill', 'Trash'),
                    ('tree-fill', 'Tree'),
                    ('trophy-fill', 'Trophy'),
                    ('truck', 'Truck'),
                    ('tv', 'TV'),
                    ('umbrella-fill', 'Umbrells'),
                    ('unlock-fill', 'Unlock'),
                    ('usb-drive-fill', 'USB'),
                    ('valentine', 'Valentine'),
                    ('vector-pen', 'Vector'),
                    ('virus2', 'Virus'),
                    ('volume-down-fill', 'Volume'),
                    ('wallet2', 'Wallet'),
                    ('watch', 'Watch'),
                    ('water', 'Water'),
                    ('webcam-fill', 'Webcam'),
                    ('wifi', 'Wi-Fi'),
                    ('wind', 'Wind'),
                    ('wrench', 'Wrench'),
                    ('yin-yang', 'Yin-Yang')
                ],
                attrs={'class': 'form-select mb-3'}
            ),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color w-100 mb-3'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'})
        }
