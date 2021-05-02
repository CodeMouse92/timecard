"""Interface [Timecard]
Author(s): Jason C. McDonald

Top-level functions for the interface sub-package. These are the functions
initially called to build and run the interface.
"""

from timecard.interface.app import App
from timecard.interface.appcontrols import AppControls
from timecard.interface.notes import Notes
from timecard.interface.timecontrols import TimeControls
from timecard.interface.timedisplay import TimeDisplay
from timecard.interface.systray import SysTray
from timecard.interface.workspace import Workspace

from timecard.data.backup import Backup

from timecard.logic.clock import Clock


def build():
    """Construct the interface."""
    App.build()
    App.add_widget(TimeDisplay.build())
    App.add_widget(Notes.build())
    App.add_widget(TimeControls.build())
    App.add_widget(Workspace.build())
    App.add_widget(AppControls.build())
    SysTray.build()

    # See if there's anything to recover from a damaged session.
    Backup.check_for_recall()
    # Start monitoring new timers.
    Backup.start_monitoring()

    Clock.start()


def run():
    """Run the interface."""
    build()
    return App.run()
