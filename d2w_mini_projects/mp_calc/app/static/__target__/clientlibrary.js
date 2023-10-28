// Transcrypt'ed from Python, 2023-10-28 19:03:16
var time = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_time__ from './time.js';
__nest__ (time, '', __module_time__);
var __name__ = '__main__';
export var AnswerTime =  __class__ ('AnswerTime', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, question_id) {
		self.id = question_id;
		self.start = time.time ();
		self.end = -(1);
	});},
	get _get_elapsedtime () {return __get__ (this, function (self) {
		if (self.end == -(1)) {
			self.stop ();
		}
		return int (self.end - self.start);
	});},
	get restart () {return __get__ (this, function (self, question_id) {
		self.id = question_id;
		self.start = time.time ();
	});},
	get stop () {return __get__ (this, function (self) {
		self.end = time.time ();
	});}
});
Object.defineProperty (AnswerTime, 'elapsedtime', property.call (AnswerTime, AnswerTime._get_elapsedtime));;
export var Records =  __class__ ('Records', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.py_items = dict ({});
	});},
	get start_timer () {return __get__ (this, function (self, question_id) {
		self.py_items [question_id] = AnswerTime (question_id);
	});},
	get stop_timer () {return __get__ (this, function (self, form_id, question_id) {
		self.py_items [question_id].stop ();
		var curform = document.getElementById ('form-{}'.format (form_id));
		var answer = curform.elements ['answer'].value;
		curform.elements ['challenge_id'].value = str (question_id);
		curform.elements ['elapsed_time'].value = self.py_items [question_id].elapsedtime;
		curform.submit ();
	});},
	get get_elapsedtime () {return __get__ (this, function (self, question_id) {
		return self.py_items [question_id].elapsedtime;
	});}
});
export var records = Records ();

//# sourceMappingURL=clientlibrary.map