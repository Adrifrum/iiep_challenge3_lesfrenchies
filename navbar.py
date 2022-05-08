from dash_bootstrap_components._components.Container import Container
from dash import Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import html
from dash import html


logo_iiep = "https://www.marketing-professionnel.fr/wp-content/uploads/2021/05/comment-adapter-campagnes-emailing-locales-solutions.jpg"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Select a country", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)


def Navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=logo_iiep, height="50px")),
                            dbc.Col(dbc.NavbarBrand(
                                "Challenge 3 : Les frenchies", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="http://www.iiep.unesco.org/fr",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )
    return navbar
