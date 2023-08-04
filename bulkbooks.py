from app import db
from app.models import Book

db.create_all()

b = [
    Book(
        image="https://img.kitapyurdu.com/v1/getImage/fn:11582810/wh:true/wi:220",
        author="Paulo Coelho",
        title="Simyacı",
        price=50.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781787637078.webp",
        author="Chris Broad",
        title="Abroad in Japan",
        price=21.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781398717237.webp",
        author="Jessa Hastings",
        title="Daisy Haites 2 The Great Undoing",
        price=17.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781398717206.webp",
        author="Jessa Hastings",
        title="Magnolia Parks",
        price=18.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781398717213.webp",
        author="Jessa Hastings",
        title="Daisy Haites",
        price=17.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781399730518.webp",
        author="Stephanie Garber",
        title="Once Upon A Broken Heart",
        price=24.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781844885428.webp",
        author="Sinéad O'Connor",
        title="Rememberings",
        price=12.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781838959708.webp",
        author="Kai Bird,",
        title="American Prometheus",
        price=19.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781537324005.webp",
        author="Benjamin J",
        title="80,000 Hours: Find a fulfilling career that does good",
        price=21.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781529399288.webp",
        author="Stephanie Garber",
        title="A Curse for True Love - Once Upon a Broken Heart",
        price=24.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781529381009.webp",
        author="Stephanie Garber",
        title="The Ballad of Never After - Once Upon a Broken Heart",
        price=13.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781529380941.webp",
        author="Stephanie Garber",
        title="Once Upon a Broken Heart",
        price=14.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781785044458.webp",
        author="Alice Gendron",
        title="The Mini ADHD Coach",
        price=21.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781638589310.webp",
        author="Priest (author),",
        title="Stars of Chaos: Sha Po Lang (Novel) Vol. 1",
        price=24.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781783350513.webp",
        author="William MacAskill",
        title="Doing Good Better",
        price=14.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781526600233.webp",
        author="Toby Ord",
        title="The Precipice Existential Risk and the Future of Humanity",
        price=16.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9780241624272.webp",
        author="Bea Fitzgerald",
        title="Girl, Goddess, Queen",
        price=21.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781472153746.webp",
        author="Mary Oliver",
        title="Blue Horses",
        price=14.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781526628220.webp",
        author="Sarah J. Maas",
        title="House of Sky and Breath",
        price=12.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9781526663559.webp",
        author="Sarah J. Maas",
        title="House of Earth and Blood",
        price=14.0
    ),
    Book(
        image="https://blackwells.co.uk/jacket/500x500/9780349436999.webp",
        author="Rebecca Yarros",
        title="Fourth Wing",
        price=28.0
    )
]

db.session.add_all(b)
db.session.commit()