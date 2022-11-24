from abc import ABCMeta, abstractmethod


class IButton(metaclass=ABCMeta):
    """Интерфейс"""
    @abstractmethod
    def render(self) -> None:
        pass


class WindowButton(IButton):
    def render(self) -> None:
        print("Показать кнопку")


class HTMLButton(IButton):
    def render(self) -> None:
        print("<h2>Показать кнопку</h2>")


class IFabric(metaclass=ABCMeta):
    @abstractmethod
    def make_button(self, button: IButton) -> IButton:
        pass


class RealFabric(IFabric):
    def make_button(self, button: IButton) -> IButton:
        return button()


if __name__ == '__main__':
    wind_fabric: IFabric = RealFabric()
    wind_button: IButton = wind_fabric.make_button(WindowButton)

    wind_button.render()

    html_fabric: IFabric = RealFabric()
    html_button: IButton = html_fabric.make_button(HTMLButton)
    html_button.render()
