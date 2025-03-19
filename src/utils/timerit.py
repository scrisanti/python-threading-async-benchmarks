from contextlib import ContextDecorator
from dataclasses import dataclass, field
from timeit import default_timer as timer
from typing import Any, Callable, ClassVar, Dict, Optional
 
from utils.setup_logging import logger
 
 
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""
 
# ------------------ Main Class Def  -------------------------
 
@dataclass
class Timer(ContextDecorator):
    """Time your code using a class, context manager, or decorator"""
 
    timers: ClassVar[Dict[str, float]] = dict()
    name: Optional[str] = None
    text: str = "{} Elapsed time: {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = logger # This is using the logger defined in setup_logging
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
 
    def __post_init__(self) -> None:
        """Initialization: add timer to dict of timers"""
        if self.name:
            self.timers.setdefault(self.name, 0)
 
    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
 
        self._start_time = timer()
 
    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
 
        # Calculate elapsed time
        elapsed_time = timer() - self._start_time
        self._start_time = None
 
        # Report elapsed time
        if self.logger:
            self.logger.debug(self.text.format(self.name,elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time
 
        return elapsed_time
 
    def __enter__(self) -> "Timer":
        """Start a new timer as a context manager"""
        self.start()
        return self
 
    def __exit__(self, *exc_info: Any) -> None:
        """Stop the context manager timer"""
        self.stop()
 
if __name__ =='__main__':
    """
    This is the test Usage function ofr TimerIt Module
   
    """
    @Timer(name='My Expensive Function')
    def myexfunc(n = 100):
        x = 0
        for i in range(n):
            x += hash(i**i)
 
    @Timer(name='My 2nd Expensive Function')
    def myexfunc2(n = 100):
        x = 0
        for i in range(n):
            x += hash(i**i)
 
    myexfunc(979)
    myexfunc2(969)
    myexfunc(959)
    myexfunc2(949)
 
    t = Timer(name='TestUsage')
    t.start()
    myexfunc(3455)
    t.stop()
    print(Timer.timers)
 