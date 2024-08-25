from flet import *
import flet_core.map as map


def main(page: Page):
    page.bgcolor = "#1F1D2B"
    page.window_width = 1024
    page.window_height = 500

    marker_layer_ref = Ref[map.MarkerLayer]()
    lat_text_ref = Ref[TextField]()
    lon_text_ref = Ref[TextField]()

    def handle_tap(e: map.MapTapEvent):
        print(f"Tapped at coordinates: {e.coordinates}")

        # Clear existing markers
        marker_layer_ref.current.markers.clear()

        # Add the new marker
        marker_layer_ref.current.markers.append(
            map.Marker(
                content=Icon(
                    name=icons.LOCATION_ON,
                    color=colors.RED,
                    size=14,
                ),
                coordinates=e.coordinates,
            )
        )

        # Update the TextField elements with the new coordinates
        lat_text_ref.current.value = f"{e.coordinates.latitude:.6f}"  # Latitude
        lon_text_ref.current.value = f"{e.coordinates.longitude:.6f}"  # Longitude

        page.update()

    def handle_event(e: map.MapEvent):
        # Hech qanday harakat qilinmaydi
        pass

    split = Container(
        margin=margin.only(left=52.8, top=17.33, right=52.8, bottom=113),
        content=Column(
            controls=[
                Container(
                    content=Image(
                        src="assets/logo.png",
                        width=140.8,
                        height=76.27,
                        fit=ImageFit.CONTAIN
                    )
                ),
                Container(
                    Divider(color="#393C49"),
                    margin=margin.only(left=15)
                ),
                Container(
                    content=Text(
                        value="Yetkazib berish",
                        color="#fafafa",
                        size=17,
                        weight=FontWeight.W_700,
                    ),
                    alignment=alignment.center
                ),
                Row(
                    controls=[
                        Container(
                            Column(
                                controls=[
                                    Text(
                                        value="Ism,Familya,Otasining ismi",
                                        size=11,
                                        weight=FontWeight.W_600,
                                        color="#FFFFFF"
                                    ),
                                    Container(
                                        TextField(
                                            border_radius=17,
                                            bgcolor="#FFFFFF",
                                            width=397,
                                            height=26.5,
                                            text_style=TextStyle(
                                                size=12,
                                                weight=FontWeight.W_600
                                            ),
                                            content_padding=padding.only(left=10, bottom=8)
                                        ),
                                    ),
                                    Container(
                                        height=8
                                    ),
                                    Text(
                                        value="Yashash manzili",
                                        size=11,
                                        weight=FontWeight.W_600,
                                        color="#FFFFFF"
                                    ),
                                    Container(
                                        TextField(
                                            border_radius=17,
                                            bgcolor="#FFFFFF",
                                            width=397,
                                            height=26.5,
                                            text_style=TextStyle(
                                                size=12,
                                                weight=FontWeight.W_600
                                            ),
                                            content_padding=padding.only(left=10, bottom=8),
                                        ),
                                    ),
                                    Container(
                                        height=8
                                    ),
                                    Text(
                                        value="Mo'jal",
                                        size=11,
                                        weight=FontWeight.W_600,
                                        color="#FFFFFF",
                                    ),
                                    Container(
                                        TextField(
                                            border_radius=17,
                                            bgcolor="#FFFFFF",
                                            width=397,
                                            height=26.5,
                                            text_style=TextStyle(
                                                size=12,
                                                weight=FontWeight.W_600
                                            ),
                                            content_padding=padding.only(left=10, bottom=8)
                                        ),
                                    ),
                                    Container(
                                        height=8
                                    ),
                                    Container(
                                        content=Row(
                                            controls=[
                                                Container(
                                                    Text(
                                                        value="Telefon raqam",
                                                        size=11,
                                                        weight=FontWeight.W_600,
                                                        color="#FFFFFF"
                                                    ),
                                                    width=150,

                                                ),
                                                Container(
                                                    Text(
                                                        value="Loc.Lan",
                                                        size=11,
                                                        weight=FontWeight.W_600,
                                                        color="#FFFFFF",

                                                    ),
                                                    width=100,

                                                    alignment=alignment.center
                                                ),
                                                Container(
                                                    Text(
                                                        value="Loc.Ant",
                                                        size=11,
                                                        weight=FontWeight.W_600,
                                                        color="#FFFFFF"
                                                    ),
                                                    width=100,

                                                    alignment=alignment.center
                                                )
                                            ],
                                            spacing=22
                                        )
                                    ),
                                    Container(
                                        Row(
                                            controls=[
                                                TextField(
                                                    border_radius=17,
                                                    bgcolor="#FFFFFF",
                                                    width=150,
                                                    height=26.5,
                                                    value="+998",
                                                    text_size=15,
                                                    keyboard_type=KeyboardType.PHONE,
                                                    text_style=TextStyle(
                                                        weight=FontWeight.W_600,
                                                    ),
                                                    content_padding=Padding(left=10, top=2, bottom=2, right=2)
                                                ),
                                                TextField(
                                                    ref=lat_text_ref,  # Latitude uchun TextField
                                                    border_radius=17,
                                                    bgcolor="#FFFFFF",
                                                    width=100,
                                                    height=26.5,
                                                    text_size=12,
                                                    read_only=True,
                                                    text_align=TextAlign.CENTER,
                                                    text_style=TextStyle(
                                                        weight=FontWeight.W_600
                                                    ),
                                                    content_padding=Padding(left=8, top=2, bottom=2, right=2)
                                                ),
                                                TextField(
                                                    ref=lon_text_ref,  # Longitude uchun TextField
                                                    border_radius=17,
                                                    bgcolor="#FFFFFF",
                                                    width=100,
                                                    height=26.5,
                                                    text_size=12,
                                                    read_only=True,
                                                    text_align=TextAlign.CENTER,
                                                    text_style=TextStyle(
                                                        weight=FontWeight.W_600,

                                                    ),
                                                    content_padding=Padding(left=8, top=2, bottom=2, right=2)
                                                )
                                            ],
                                            spacing=22
                                        )
                                    ),
                                    Container(
                                        height=12
                                    ),
                                    Container(

                                        content=Row(
                                            controls=[
                                                TextButton(
                                                    content=Row(
                                                        controls=[
                                                            Container(
                                                                Icon(
                                                                    name=icons.CHECK,
                                                                    color="#FFFFFF",
                                                                    size=12,
                                                                ),
                                                                margin=margin.only(top=3)
                                                            ),
                                                            Text(
                                                                value=" Ma'lumotlarni saqlash",
                                                                size=13,
                                                                color="#FFFFFF",
                                                                weight=FontWeight.W_600,
                                                                text_align=TextAlign.CENTER,
                                                                height=18,
                                                            ),
                                                        ],
                                                        spacing=0,
                                                        alignment=MainAxisAlignment.CENTER,
                                                        vertical_alignment=CrossAxisAlignment.CENTER
                                                    ),
                                                    width=192,
                                                    height=26.5,
                                                    style=ButtonStyle(
                                                        bgcolor="#EA7C69",
                                                        shape=RoundedRectangleBorder(radius=17),
                                                    )
                                                )
                                            ],
                                            width=393,
                                            alignment=MainAxisAlignment.END
                                        )
                                    )
                                ],
                                spacing=0
                            ),
                            margin=margin.only(left=43.73, bottom=9.5)
                        ),
                        Container(
                            content=map.Map(
                                width=400,
                                height=230,
                                configuration=map.MapConfiguration(
                                    initial_center=map.MapLatitudeLongitude(41.2995, 69.2401),
                                    # Tashkent shahrining koordinatalari
                                    initial_zoom=12.0,
                                    interaction_configuration=map.MapInteractionConfiguration(
                                        flags=map.MapInteractiveFlag.ALL
                                    ),
                                    on_init=lambda e: print(f"Initialized Map"),
                                    on_event=handle_event,
                                    on_tap=handle_tap,  # Mana bu yerda on_tap event qo'shildi
                                ),
                                layers=[
                                    map.TileLayer(
                                        url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                        on_image_error=lambda e: print("TileLayer Error"),
                                    ),
                                    map.MarkerLayer(
                                        ref=marker_layer_ref,
                                        markers=[],  # Bu yerda markerlar ro'yxatini bo'sh qoldirdik
                                    ),
                                ],
                            ),
                            border_radius=8.5,
                            margin=margin.only(left=20, top=10, bottom=16),
                        ),
                    ],
                )
            ],
            spacing=0
        ),
    )
    page.add(
        Column(
            controls=[split],
            expand=True
        )
    )


app(target=main, assets_dir="assets")
