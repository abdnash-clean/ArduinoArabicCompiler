// Generated from e:/projects/ArduinoArabicCompiler/ArArduinoParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ArArduinoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, IF=2, ELSE=3, WHILE=4, TRUE=5, FALSE=6, INT_T=7, FLOAT_T=8, VOID=9, 
		FUNCTION=10, RETURN=11, SETUP=12, LOOP=13, BOOL=14, ASSIGN=15, PLUS=16, 
		MINUS=17, MUL=18, DIV=19, GT=20, LT=21, OR=22, AND=23, LPAREN=24, RPAREN=25, 
		LBRACE=26, RBRACE=27, COLON=28, SEMI=29, COMA=30, NUMBER=31, ID=32, WS=33, 
		LINE_COMMENT=34;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_setupDec = 2, RULE_loopDec = 3, 
		RULE_funDecl = 4, RULE_varDecl = 5, RULE_params = 6, RULE_param = 7, RULE_block = 8, 
		RULE_statement = 9, RULE_assignment = 10, RULE_ifStat = 11, RULE_whileStat = 12, 
		RULE_returnStat = 13, RULE_funcCall = 14, RULE_args = 15, RULE_expression = 16, 
		RULE_primary = 17, RULE_type = 18;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "setupDec", "loopDec", "funDecl", "varDecl", 
			"params", "param", "block", "statement", "assignment", "ifStat", "whileStat", 
			"returnStat", "funcCall", "args", "expression", "primary", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0645\\u062A\\u063A\\u064A\\u0631'", null, null, "'\\u0637\\u0627\\u0644\\u0645\\u0627'", 
			"'\\u0635\\u062D'", "'\\u063A\\u0644\\u0637'", "'\\u0635\\u062D\\u064A\\u062D'", 
			"'\\u0639\\u0634\\u0631\\u064A'", "'\\u0641\\u0627\\u0631\\u063A'", "'\\u062F\\u0627\\u0644\\u0629'", 
			"'\\u0627\\u0631\\u062C\\u0639'", "'\\u0625\\u0639\\u062F\\u0627\\u062F'", 
			"'\\u062A\\u0643\\u0631\\u0627\\u0631'", "'\\u0645\\u0646\\u0637\\u0642\\u064A'", 
			"'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'\\u0623\\u0648'", 
			"'\\u0648'", "'('", "')'", "'{'", "'}'", "':'", "'\\u061B'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "IF", "ELSE", "WHILE", "TRUE", "FALSE", "INT_T", "FLOAT_T", 
			"VOID", "FUNCTION", "RETURN", "SETUP", "LOOP", "BOOL", "ASSIGN", "PLUS", 
			"MINUS", "MUL", "DIV", "GT", "LT", "OR", "AND", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "COLON", "SEMI", "COMA", "NUMBER", "ID", "WS", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ArArduinoParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ArArduinoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ArArduinoParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==FUNCTION) {
				{
				{
				setState(38);
				declaration();
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(44);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public SetupDecContext setupDec() {
			return getRuleContext(SetupDecContext.class,0);
		}
		public LoopDecContext loopDec() {
			return getRuleContext(LoopDecContext.class,0);
		}
		public FunDeclContext funDecl() {
			return getRuleContext(FunDeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(50);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				varDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				setupDec();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				loopDec();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(49);
				funDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetupDecContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(ArArduinoParser.FUNCTION, 0); }
		public TerminalNode SETUP() { return getToken(ArArduinoParser.SETUP, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TerminalNode VOID() { return getToken(ArArduinoParser.VOID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public SetupDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setupDec; }
	}

	public final SetupDecContext setupDec() throws RecognitionException {
		SetupDecContext _localctx = new SetupDecContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_setupDec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(FUNCTION);
			setState(53);
			match(SETUP);
			setState(54);
			match(LPAREN);
			setState(55);
			match(RPAREN);
			setState(56);
			match(COLON);
			setState(57);
			match(VOID);
			setState(58);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopDecContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(ArArduinoParser.FUNCTION, 0); }
		public TerminalNode LOOP() { return getToken(ArArduinoParser.LOOP, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TerminalNode VOID() { return getToken(ArArduinoParser.VOID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public LoopDecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopDec; }
	}

	public final LoopDecContext loopDec() throws RecognitionException {
		LoopDecContext _localctx = new LoopDecContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_loopDec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(FUNCTION);
			setState(61);
			match(LOOP);
			setState(62);
			match(LPAREN);
			setState(63);
			match(RPAREN);
			setState(64);
			match(COLON);
			setState(65);
			match(VOID);
			setState(66);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunDeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(ArArduinoParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public FunDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funDecl; }
	}

	public final FunDeclContext funDecl() throws RecognitionException {
		FunDeclContext _localctx = new FunDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(FUNCTION);
			setState(69);
			match(ID);
			setState(70);
			match(LPAREN);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(71);
				params();
				}
			}

			setState(74);
			match(RPAREN);
			setState(75);
			match(COLON);
			setState(76);
			type();
			setState(77);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(ArArduinoParser.VAR, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(ArArduinoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ArArduinoParser.SEMI, 0); }
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(VAR);
			setState(80);
			match(ID);
			setState(81);
			match(COLON);
			setState(82);
			type();
			setState(83);
			match(ASSIGN);
			setState(84);
			expression(0);
			setState(85);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(ArArduinoParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ArArduinoParser.COMA, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			param();
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(88);
				match(COMA);
				setState(89);
				param();
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(ID);
			setState(96);
			match(COLON);
			setState(97);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(ArArduinoParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ArArduinoParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(LBRACE);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294969366L) != 0)) {
				{
				{
				setState(100);
				statement();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ArArduinoParser.SEMI, 0); }
		public FuncCallContext funcCall() {
			return getRuleContext(FuncCallContext.class,0);
		}
		public IfStatContext ifStat() {
			return getRuleContext(IfStatContext.class,0);
		}
		public WhileStatContext whileStat() {
			return getRuleContext(WhileStatContext.class,0);
		}
		public ReturnStatContext returnStat() {
			return getRuleContext(ReturnStatContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(120);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				varDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				assignment();
				setState(110);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				funcCall();
				setState(113);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(115);
				ifStat();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(116);
				whileStat();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(117);
				returnStat();
				setState(118);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(ArArduinoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(ID);
			setState(123);
			match(ASSIGN);
			setState(124);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(ArArduinoParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ArArduinoParser.ELSE, 0); }
		public IfStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStat; }
	}

	public final IfStatContext ifStat() throws RecognitionException {
		IfStatContext _localctx = new IfStatContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(IF);
			setState(127);
			match(LPAREN);
			setState(128);
			expression(0);
			setState(129);
			match(RPAREN);
			setState(130);
			block();
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(131);
				match(ELSE);
				setState(132);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(ArArduinoParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStat; }
	}

	public final WhileStatContext whileStat() throws RecognitionException {
		WhileStatContext _localctx = new WhileStatContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_whileStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(WHILE);
			setState(136);
			match(LPAREN);
			setState(137);
			expression(0);
			setState(138);
			match(RPAREN);
			setState(139);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(ArArduinoParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStat; }
	}

	public final ReturnStatContext returnStat() throws RecognitionException {
		ReturnStatContext _localctx = new ReturnStatContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_returnStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(RETURN);
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 6459359328L) != 0)) {
				{
				setState(142);
				expression(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public FuncCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcCall; }
	}

	public final FuncCallContext funcCall() throws RecognitionException {
		FuncCallContext _localctx = new FuncCallContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_funcCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(ID);
			setState(146);
			match(LPAREN);
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 6459359328L) != 0)) {
				{
				setState(147);
				args();
				}
			}

			setState(150);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(ArArduinoParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ArArduinoParser.COMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			expression(0);
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(153);
				match(COMA);
				setState(154);
				expression(0);
				}
				}
				setState(159);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExprContext extends ExpressionContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public PrimaryExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryMinusExprContext extends ExpressionContext {
		public TerminalNode MINUS() { return getToken(ArArduinoParser.MINUS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public UnaryMinusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelOpExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GT() { return getToken(ArArduinoParser.GT, 0); }
		public TerminalNode LT() { return getToken(ArArduinoParser.LT, 0); }
		public RelOpExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PlusMinusExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(ArArduinoParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ArArduinoParser.MINUS, 0); }
		public PlusMinusExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(ArArduinoParser.OR, 0); }
		public OrExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallExprContext extends ExpressionContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public FuncCallExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensExprContext extends ExpressionContext {
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public ParensExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(ArArduinoParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ArArduinoParser.DIV, 0); }
		public MulDivExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(ArArduinoParser.AND, 0); }
		public AndExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				_localctx = new PrimaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(161);
				primary();
				}
				break;
			case 2:
				{
				_localctx = new FuncCallExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(162);
				match(ID);
				setState(163);
				match(LPAREN);
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 6459359328L) != 0)) {
					{
					setState(164);
					args();
					}
				}

				setState(167);
				match(RPAREN);
				}
				break;
			case 3:
				{
				_localctx = new ParensExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(168);
				match(LPAREN);
				setState(169);
				expression(0);
				setState(170);
				match(RPAREN);
				}
				break;
			case 4:
				{
				_localctx = new UnaryMinusExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(172);
				match(MINUS);
				setState(173);
				expression(6);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(193);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(191);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(176);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(177);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(178);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new PlusMinusExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(179);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(180);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(181);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new RelOpExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(182);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(183);
						_la = _input.LA(1);
						if ( !(_la==GT || _la==LT) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(184);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new AndExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(185);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(186);
						match(AND);
						setState(187);
						expression(3);
						}
						break;
					case 5:
						{
						_localctx = new OrExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(188);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(189);
						match(OR);
						setState(190);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(195);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(ArArduinoParser.NUMBER, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode TRUE() { return getToken(ArArduinoParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(ArArduinoParser.FALSE, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primary);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 6442451040L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_T() { return getToken(ArArduinoParser.INT_T, 0); }
		public TerminalNode FLOAT_T() { return getToken(ArArduinoParser.FLOAT_T, 0); }
		public TerminalNode VOID() { return getToken(ArArduinoParser.VOID, 0); }
		public TerminalNode BOOL() { return getToken(ArArduinoParser.BOOL, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17280L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\"\u00c9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"3\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004I\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006[\b\u0006\n\u0006\f\u0006"+
		"^\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0005\bf\b\b\n\b\f\bi\t\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\ty\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0086"+
		"\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0003\r\u0090\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0095"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005"+
		"\u000f\u009c\b\u000f\n\u000f\f\u000f\u009f\t\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00a6\b\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00af\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010"+
		"\u00c0\b\u0010\n\u0010\f\u0010\u00c3\t\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0000\u0001 \u0013\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$\u0000"+
		"\u0005\u0001\u0000\u0012\u0013\u0001\u0000\u0010\u0011\u0001\u0000\u0014"+
		"\u0015\u0002\u0000\u0005\u0006\u001f \u0002\u0000\u0007\t\u000e\u000e"+
		"\u00ce\u0000)\u0001\u0000\u0000\u0000\u00022\u0001\u0000\u0000\u0000\u0004"+
		"4\u0001\u0000\u0000\u0000\u0006<\u0001\u0000\u0000\u0000\bD\u0001\u0000"+
		"\u0000\u0000\nO\u0001\u0000\u0000\u0000\fW\u0001\u0000\u0000\u0000\u000e"+
		"_\u0001\u0000\u0000\u0000\u0010c\u0001\u0000\u0000\u0000\u0012x\u0001"+
		"\u0000\u0000\u0000\u0014z\u0001\u0000\u0000\u0000\u0016~\u0001\u0000\u0000"+
		"\u0000\u0018\u0087\u0001\u0000\u0000\u0000\u001a\u008d\u0001\u0000\u0000"+
		"\u0000\u001c\u0091\u0001\u0000\u0000\u0000\u001e\u0098\u0001\u0000\u0000"+
		"\u0000 \u00ae\u0001\u0000\u0000\u0000\"\u00c4\u0001\u0000\u0000\u0000"+
		"$\u00c6\u0001\u0000\u0000\u0000&(\u0003\u0002\u0001\u0000\'&\u0001\u0000"+
		"\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001"+
		"\u0000\u0000\u0000*,\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		",-\u0005\u0000\u0000\u0001-\u0001\u0001\u0000\u0000\u0000.3\u0003\n\u0005"+
		"\u0000/3\u0003\u0004\u0002\u000003\u0003\u0006\u0003\u000013\u0003\b\u0004"+
		"\u00002.\u0001\u0000\u0000\u00002/\u0001\u0000\u0000\u000020\u0001\u0000"+
		"\u0000\u000021\u0001\u0000\u0000\u00003\u0003\u0001\u0000\u0000\u0000"+
		"45\u0005\n\u0000\u000056\u0005\f\u0000\u000067\u0005\u0018\u0000\u0000"+
		"78\u0005\u0019\u0000\u000089\u0005\u001c\u0000\u00009:\u0005\t\u0000\u0000"+
		":;\u0003\u0010\b\u0000;\u0005\u0001\u0000\u0000\u0000<=\u0005\n\u0000"+
		"\u0000=>\u0005\r\u0000\u0000>?\u0005\u0018\u0000\u0000?@\u0005\u0019\u0000"+
		"\u0000@A\u0005\u001c\u0000\u0000AB\u0005\t\u0000\u0000BC\u0003\u0010\b"+
		"\u0000C\u0007\u0001\u0000\u0000\u0000DE\u0005\n\u0000\u0000EF\u0005 \u0000"+
		"\u0000FH\u0005\u0018\u0000\u0000GI\u0003\f\u0006\u0000HG\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JK\u0005\u0019"+
		"\u0000\u0000KL\u0005\u001c\u0000\u0000LM\u0003$\u0012\u0000MN\u0003\u0010"+
		"\b\u0000N\t\u0001\u0000\u0000\u0000OP\u0005\u0001\u0000\u0000PQ\u0005"+
		" \u0000\u0000QR\u0005\u001c\u0000\u0000RS\u0003$\u0012\u0000ST\u0005\u000f"+
		"\u0000\u0000TU\u0003 \u0010\u0000UV\u0005\u001d\u0000\u0000V\u000b\u0001"+
		"\u0000\u0000\u0000W\\\u0003\u000e\u0007\u0000XY\u0005\u001e\u0000\u0000"+
		"Y[\u0003\u000e\u0007\u0000ZX\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000"+
		"\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\r\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_`\u0005 \u0000\u0000`a\u0005"+
		"\u001c\u0000\u0000ab\u0003$\u0012\u0000b\u000f\u0001\u0000\u0000\u0000"+
		"cg\u0005\u001a\u0000\u0000df\u0003\u0012\t\u0000ed\u0001\u0000\u0000\u0000"+
		"fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000"+
		"\u0000hj\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000jk\u0005\u001b"+
		"\u0000\u0000k\u0011\u0001\u0000\u0000\u0000ly\u0003\n\u0005\u0000mn\u0003"+
		"\u0014\n\u0000no\u0005\u001d\u0000\u0000oy\u0001\u0000\u0000\u0000pq\u0003"+
		"\u001c\u000e\u0000qr\u0005\u001d\u0000\u0000ry\u0001\u0000\u0000\u0000"+
		"sy\u0003\u0016\u000b\u0000ty\u0003\u0018\f\u0000uv\u0003\u001a\r\u0000"+
		"vw\u0005\u001d\u0000\u0000wy\u0001\u0000\u0000\u0000xl\u0001\u0000\u0000"+
		"\u0000xm\u0001\u0000\u0000\u0000xp\u0001\u0000\u0000\u0000xs\u0001\u0000"+
		"\u0000\u0000xt\u0001\u0000\u0000\u0000xu\u0001\u0000\u0000\u0000y\u0013"+
		"\u0001\u0000\u0000\u0000z{\u0005 \u0000\u0000{|\u0005\u000f\u0000\u0000"+
		"|}\u0003 \u0010\u0000}\u0015\u0001\u0000\u0000\u0000~\u007f\u0005\u0002"+
		"\u0000\u0000\u007f\u0080\u0005\u0018\u0000\u0000\u0080\u0081\u0003 \u0010"+
		"\u0000\u0081\u0082\u0005\u0019\u0000\u0000\u0082\u0085\u0003\u0010\b\u0000"+
		"\u0083\u0084\u0005\u0003\u0000\u0000\u0084\u0086\u0003\u0010\b\u0000\u0085"+
		"\u0083\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086"+
		"\u0017\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u0004\u0000\u0000\u0088"+
		"\u0089\u0005\u0018\u0000\u0000\u0089\u008a\u0003 \u0010\u0000\u008a\u008b"+
		"\u0005\u0019\u0000\u0000\u008b\u008c\u0003\u0010\b\u0000\u008c\u0019\u0001"+
		"\u0000\u0000\u0000\u008d\u008f\u0005\u000b\u0000\u0000\u008e\u0090\u0003"+
		" \u0010\u0000\u008f\u008e\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000"+
		"\u0000\u0000\u0090\u001b\u0001\u0000\u0000\u0000\u0091\u0092\u0005 \u0000"+
		"\u0000\u0092\u0094\u0005\u0018\u0000\u0000\u0093\u0095\u0003\u001e\u000f"+
		"\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000"+
		"\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0097\u0005\u0019\u0000"+
		"\u0000\u0097\u001d\u0001\u0000\u0000\u0000\u0098\u009d\u0003 \u0010\u0000"+
		"\u0099\u009a\u0005\u001e\u0000\u0000\u009a\u009c\u0003 \u0010\u0000\u009b"+
		"\u0099\u0001\u0000\u0000\u0000\u009c\u009f\u0001\u0000\u0000\u0000\u009d"+
		"\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000\u009e"+
		"\u001f\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u00a0"+
		"\u00a1\u0006\u0010\uffff\uffff\u0000\u00a1\u00af\u0003\"\u0011\u0000\u00a2"+
		"\u00a3\u0005 \u0000\u0000\u00a3\u00a5\u0005\u0018\u0000\u0000\u00a4\u00a6"+
		"\u0003\u001e\u000f\u0000\u00a5\u00a4\u0001\u0000\u0000\u0000\u00a5\u00a6"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00af"+
		"\u0005\u0019\u0000\u0000\u00a8\u00a9\u0005\u0018\u0000\u0000\u00a9\u00aa"+
		"\u0003 \u0010\u0000\u00aa\u00ab\u0005\u0019\u0000\u0000\u00ab\u00af\u0001"+
		"\u0000\u0000\u0000\u00ac\u00ad\u0005\u0011\u0000\u0000\u00ad\u00af\u0003"+
		" \u0010\u0006\u00ae\u00a0\u0001\u0000\u0000\u0000\u00ae\u00a2\u0001\u0000"+
		"\u0000\u0000\u00ae\u00a8\u0001\u0000\u0000\u0000\u00ae\u00ac\u0001\u0000"+
		"\u0000\u0000\u00af\u00c1\u0001\u0000\u0000\u0000\u00b0\u00b1\n\u0005\u0000"+
		"\u0000\u00b1\u00b2\u0007\u0000\u0000\u0000\u00b2\u00c0\u0003 \u0010\u0006"+
		"\u00b3\u00b4\n\u0004\u0000\u0000\u00b4\u00b5\u0007\u0001\u0000\u0000\u00b5"+
		"\u00c0\u0003 \u0010\u0005\u00b6\u00b7\n\u0003\u0000\u0000\u00b7\u00b8"+
		"\u0007\u0002\u0000\u0000\u00b8\u00c0\u0003 \u0010\u0004\u00b9\u00ba\n"+
		"\u0002\u0000\u0000\u00ba\u00bb\u0005\u0017\u0000\u0000\u00bb\u00c0\u0003"+
		" \u0010\u0003\u00bc\u00bd\n\u0001\u0000\u0000\u00bd\u00be\u0005\u0016"+
		"\u0000\u0000\u00be\u00c0\u0003 \u0010\u0002\u00bf\u00b0\u0001\u0000\u0000"+
		"\u0000\u00bf\u00b3\u0001\u0000\u0000\u0000\u00bf\u00b6\u0001\u0000\u0000"+
		"\u0000\u00bf\u00b9\u0001\u0000\u0000\u0000\u00bf\u00bc\u0001\u0000\u0000"+
		"\u0000\u00c0\u00c3\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2!\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00c5\u0007\u0003\u0000\u0000"+
		"\u00c5#\u0001\u0000\u0000\u0000\u00c6\u00c7\u0007\u0004\u0000\u0000\u00c7"+
		"%\u0001\u0000\u0000\u0000\u000e)2H\\gx\u0085\u008f\u0094\u009d\u00a5\u00ae"+
		"\u00bf\u00c1";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}